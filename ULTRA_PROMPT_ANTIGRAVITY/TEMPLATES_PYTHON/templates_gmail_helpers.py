"""
Ultra Prompt v6.1 — Helper centralizado para Gmail via Maton Gateway.

Funcoes avancadas de envio com suporte a CC, BCC, reply threading,
anexos locais e template padronizado de conclusao de sessao.

Uso: from templates.gmail_helpers import gmail_send, gmail_send_with_files
"""

import urllib.request
import os
import re
import json
import base64
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime


MATON_KEY = os.environ.get('MATON_API_KEY', '')
GMAIL_URL = 'https://gateway.maton.ai/google-mail/gmail/v1/users/me/messages/send'

_EMAIL_RE = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')


# ---------------------------------------------------------------------------
# Utilidades internas
# ---------------------------------------------------------------------------

def _validar_email(email: str) -> bool:
    """Valida formato basico de endereco de email."""
    return bool(_EMAIL_RE.match(email.strip()))


def _validar_destinatarios(to, cc=None, bcc=None):
    """
    Valida que existe pelo menos um destinatario e que todos os enderecos
    possuem formato valido. Levanta ValueError se houver problema.
    """
    if not to:
        raise ValueError("Destinatario (to) e obrigatorio. Nao e possivel enviar sem destinatario.")

    todos = [to] if isinstance(to, str) else list(to)
    for campo, nome in [(cc, 'CC'), (bcc, 'BCC')]:
        if campo:
            if isinstance(campo, str):
                todos.append(campo)
            else:
                todos.extend(campo)

    for addr in todos:
        addr = addr.strip()
        if not _validar_email(addr):
            raise ValueError(f"Endereco de email invalido: {addr}")


def _normalizar_lista(valor):
    """Converte string ou lista em string separada por virgulas para headers."""
    if valor is None:
        return None
    if isinstance(valor, str):
        return valor.strip()
    return ', '.join(v.strip() for v in valor)


def _construir_mensagem(
    to,
    subject,
    body_html,
    cc=None,
    bcc=None,
    reply_to_message_id=None,
    attachments_paths=None,
):
    """
    Constroi objeto MIMEMultipart completo.

    Retorna:
        MIMEMultipart pronto para encoding e envio.
    """
    tem_anexo = attachments_paths and len(attachments_paths) > 0

    if tem_anexo:
        msg = MIMEMultipart('mixed')
        corpo = MIMEMultipart('alternative')
        corpo.attach(MIMEText(body_html, 'html', 'utf-8'))
        msg.attach(corpo)
    else:
        msg = MIMEMultipart('alternative')
        msg.attach(MIMEText(body_html, 'html', 'utf-8'))

    # Headers obrigatorios
    msg['To'] = _normalizar_lista(to)
    msg['Subject'] = subject

    # Headers opcionais
    if cc:
        msg['Cc'] = _normalizar_lista(cc)
    if bcc:
        msg['Bcc'] = _normalizar_lista(bcc)

    # Reply threading — requer In-Reply-To e References
    if reply_to_message_id:
        msg['In-Reply-To'] = reply_to_message_id
        msg['References'] = reply_to_message_id

    # Anexos
    if tem_anexo:
        for fpath in attachments_paths:
            if not os.path.isfile(fpath):
                raise FileNotFoundError(f"Arquivo nao encontrado: {fpath}")
            filename = os.path.basename(fpath)
            mime_type, _ = mimetypes.guess_type(fpath)
            if mime_type:
                maintype, subtype = mime_type.split('/', 1)
            else:
                maintype, subtype = 'application', 'octet-stream'

            with open(fpath, 'rb') as f:
                part = MIMEBase(maintype, subtype)
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename="{filename}"',
                )
                msg.attach(part)

    return msg


def _enviar_raw(msg: MIMEMultipart) -> dict:
    """
    Codifica mensagem MIME em base64url e envia via Maton Gateway.

    Retorna:
        dict com resposta da API do Gmail (contem 'id', 'threadId', 'labelIds').

    Levanta:
        urllib.error.HTTPError em caso de falha na API.
        EnvironmentError se MATON_API_KEY nao estiver configurada.
    """
    if not MATON_KEY:
        raise EnvironmentError(
            "MATON_API_KEY nao encontrada. Verifique a variavel de ambiente."
        )

    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode('utf-8')
    data = json.dumps({'raw': raw}).encode('utf-8')

    req = urllib.request.Request(GMAIL_URL, data=data, method='POST')
    req.add_header('Authorization', f'Bearer {MATON_KEY}')
    req.add_header('Content-Type', 'application/json')

    response = json.load(urllib.request.urlopen(req))
    return response


# ---------------------------------------------------------------------------
# Funcoes publicas
# ---------------------------------------------------------------------------

def gmail_send(
    to,
    subject,
    body_html,
    cc=None,
    bcc=None,
    reply_to_message_id=None,
):
    """
    Envia email via Gmail + Maton Gateway com suporte completo a CC, BCC
    e reply threading.

    Args:
        to: Destinatario principal (str ou lista de str).
        subject: Assunto do email.
        body_html: Corpo do email em HTML.
        cc: (Opcional) Destinatarios em copia (str ou lista de str).
        bcc: (Opcional) Destinatarios em copia oculta (str ou lista de str).
        reply_to_message_id: (Opcional) Message-ID RFC 2822 da mensagem
            original para encadear a resposta na mesma thread
            (define In-Reply-To e References).

    Returns:
        dict: Resposta da API do Gmail (contem 'id' e 'threadId').

    Raises:
        ValueError: Se destinatario estiver ausente ou email invalido.
        EnvironmentError: Se MATON_API_KEY nao estiver configurada.
    """
    _validar_destinatarios(to, cc, bcc)
    msg = _construir_mensagem(
        to=to,
        subject=subject,
        body_html=body_html,
        cc=cc,
        bcc=bcc,
        reply_to_message_id=reply_to_message_id,
    )
    return _enviar_raw(msg)


def gmail_send_with_files(
    to,
    subject,
    body_html,
    file_paths=None,
    cc=None,
    bcc=None,
):
    """
    Envia email com anexos locais via Gmail + Maton Gateway.

    Constroi mensagem multipart/mixed com corpo HTML e arquivos anexados.
    Detecta MIME type automaticamente para cada arquivo.

    Args:
        to: Destinatario principal (str ou lista de str).
        subject: Assunto do email.
        body_html: Corpo do email em HTML.
        file_paths: (Opcional) Lista de caminhos absolutos dos arquivos a anexar.
        cc: (Opcional) Destinatarios em copia (str ou lista de str).
        bcc: (Opcional) Destinatarios em copia oculta (str ou lista de str).

    Returns:
        dict: Resposta da API do Gmail (contem 'id' e 'threadId').

    Raises:
        ValueError: Se destinatario estiver ausente ou email invalido.
        FileNotFoundError: Se algum arquivo nao existir.
        EnvironmentError: Se MATON_API_KEY nao estiver configurada.
    """
    _validar_destinatarios(to, cc, bcc)
    msg = _construir_mensagem(
        to=to,
        subject=subject,
        body_html=body_html,
        cc=cc,
        bcc=bcc,
        attachments_paths=file_paths,
    )
    return _enviar_raw(msg)


def gmail_send_session_summary(
    to,
    session_id,
    resumo,
    file_paths=None,
):
    """
    Envia email com template padronizado de conclusao de sessao.

    Gera um HTML formatado com cabecalho, resumo da sessao, lista de
    arquivos entregues e rodape com timestamp.

    Args:
        to: Destinatario principal (str ou lista de str).
        session_id: Identificador da sessao (ex: 'task_abc123').
        resumo: Texto resumido do que foi realizado na sessao.
        file_paths: (Opcional) Lista de caminhos absolutos dos arquivos
            a anexar como entregaveis.

    Returns:
        dict: Resposta da API do Gmail (contem 'id' e 'threadId').

    Raises:
        ValueError: Se destinatario estiver ausente ou email invalido.
        FileNotFoundError: Se algum arquivo nao existir.
        EnvironmentError: Se MATON_API_KEY nao estiver configurada.
    """
    agora = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')

    # Montar lista de arquivos para o template
    arquivos_html = ''
    if file_paths:
        itens = ''.join(
            f'<li>{os.path.basename(fp)}</li>' for fp in file_paths
        )
        arquivos_html = f"""
        <h3 style="color:#333;">Arquivos entregues</h3>
        <ul>{itens}</ul>
        """

    body_html = f"""
    <div style="font-family:Arial,sans-serif;max-width:600px;margin:0 auto;
                padding:20px;border:1px solid #e0e0e0;border-radius:8px;">
        <h2 style="color:#1a73e8;border-bottom:2px solid #1a73e8;
                   padding-bottom:8px;">
            Conclusao de Sessao
        </h2>
        <table style="width:100%;margin:12px 0;font-size:14px;">
            <tr>
                <td style="padding:4px 8px;font-weight:bold;color:#555;">
                    Sessao:
                </td>
                <td style="padding:4px 8px;">{session_id}</td>
            </tr>
            <tr>
                <td style="padding:4px 8px;font-weight:bold;color:#555;">
                    Data/hora:
                </td>
                <td style="padding:4px 8px;">{agora}</td>
            </tr>
        </table>
        <h3 style="color:#333;">Resumo</h3>
        <p style="font-size:14px;line-height:1.6;color:#444;">
            {resumo}
        </p>
        {arquivos_html}
        <hr style="border:none;border-top:1px solid #e0e0e0;margin:20px 0;">
        <p style="font-size:11px;color:#999;text-align:center;">
            Enviado automaticamente por Maton Tasks — Ultra Prompt v6.1
        </p>
    </div>
    """

    subject = f'[Maton] Conclusao de sessao — {session_id}'

    return gmail_send_with_files(
        to=to,
        subject=subject,
        body_html=body_html,
        file_paths=file_paths,
    )


# ---------------------------------------------------------------------------
# Exemplo de uso
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    # 1) Envio simples com CC
    r = gmail_send(
        to='destinatario@email.com',
        subject='Teste v6.1',
        body_html='<p>Email de teste com <b>HTML</b>.</p>',
        cc='copia@email.com',
    )
    print(f"Enviado! ID: {r.get('id')}")

    # 2) Envio com anexos
    r = gmail_send_with_files(
        to='destinatario@email.com',
        subject='Relatorio com anexos',
        body_html='<p>Segue relatorio em anexo.</p>',
        file_paths=['/tmp/relatorio.pdf'],
    )
    print(f"Com anexo! ID: {r.get('id')}")

    # 3) Resumo de sessao
    r = gmail_send_session_summary(
        to='destinatario@email.com',
        session_id='task_abc123',
        resumo='Planilha financeira gerada e validada com sucesso.',
        file_paths=['/tmp/financeiro.xlsx'],
    )
    print(f"Resumo enviado! ID: {r.get('id')}")
