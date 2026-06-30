"""
Ultra Prompt v6.0 — Template: Envio de Email via Gmail + Maton Gateway
Uso: importar funcoes ou copiar/adaptar conforme necessidade da sessao.
"""

import urllib.request
import os
import json
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


MATON_KEY = os.environ.get('MATON_API_KEY', '')
GMAIL_URL = 'https://gateway.maton.ai/google-mail/gmail/v1/users/me/messages/send'


def send_email(to, subject, body_text, body_html=None, from_email=None, attachments=None):
    """
    Envia email via Gmail + Maton Gateway.

    Args:
        to: Email do destinatario.
        subject: Assunto do email.
        body_text: Corpo em texto puro.
        body_html: (Opcional) Corpo em HTML.
        from_email: (Opcional) Email do remetente (default: conta conectada).
        attachments: (Opcional) Lista de dicts com 'filepath' e 'filename'.
                     Ex: [{'filepath': '/path/to/file.pdf', 'filename': 'report.pdf'}]

    Returns:
        dict: Resposta da API do Gmail (contém 'id' e 'threadId' da mensagem).
    """
    msg = MIMEMultipart('mixed')
    msg['To'] = to
    msg['Subject'] = subject
    if from_email:
        msg['From'] = from_email

    # Corpo do email (texto + HTML)
    if body_html:
        body_part = MIMEMultipart('alternative')
        body_part.attach(MIMEText(body_text, 'plain', 'utf-8'))
        body_part.attach(MIMEText(body_html, 'html', 'utf-8'))
        msg.attach(body_part)
    else:
        msg.attach(MIMEText(body_text, 'plain', 'utf-8'))

    # Anexos
    if attachments:
        for att in attachments:
            filepath = att['filepath']
            filename = att.get('filename', os.path.basename(filepath))
            with open(filepath, 'rb') as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
                msg.attach(part)

    # Enviar via Maton Gateway
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode('utf-8')
    data = json.dumps({'raw': raw}).encode('utf-8')

    req = urllib.request.Request(GMAIL_URL, data=data, method='POST')
    req.add_header('Authorization', f'Bearer {MATON_KEY}')
    req.add_header('Content-Type', 'application/json')

    response = json.load(urllib.request.urlopen(req))
    return response


def send_simple_email(to, subject, body_text, from_email=None):
    """Atalho para email simples sem HTML nem anexos."""
    return send_email(to, subject, body_text, from_email=from_email)


def send_email_with_file(to, subject, body_text, filepath, filename=None, from_email=None):
    """Atalho para email com um unico anexo."""
    attachment = {'filepath': filepath, 'filename': filename or os.path.basename(filepath)}
    return send_email(to, subject, body_text, attachments=[attachment], from_email=from_email)


# --- Exemplo de uso ---
if __name__ == '__main__':
    # Email simples
    result = send_simple_email(
        to='destinatario@email.com',
        subject='Teste Ultra Prompt v6.0',
        body_text='Este e um email de teste enviado pelo Ultra Prompt v6.0.'
    )
    print(f"Email enviado! ID: {result.get('id')}")

    # Email com anexo
    result = send_email_with_file(
        to='destinatario@email.com',
        subject='Relatorio',
        body_text='Segue o relatorio em anexo.',
        filepath='/path/to/report.pdf'
    )
    print(f"Email com anexo enviado! ID: {result.get('id')}")
