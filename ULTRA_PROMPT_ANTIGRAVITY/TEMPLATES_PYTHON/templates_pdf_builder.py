"""
pdf_builder.py — Ultra Prompt v6.1
Construtor profissional de documentos PDF a partir de HTML ou Markdown.

Exports:
    - build_pdf_from_html(html_string, output_path, config=None) -> str
    - build_pdf_from_markdown(md_string, output_path, config=None) -> str

Dependencias: weasyprint, markdown
"""

__all__ = ["build_pdf_from_html", "build_pdf_from_markdown"]

import os
from typing import Any, Dict, Optional

import markdown

# WeasyPrint requer bibliotecas de sistema (libpango, libcairo, etc.).
# Import lazy para nao falhar no momento do import do modulo.
_weasyprint_HTML = None


def _get_weasyprint_html():
    """Importa WeasyPrint sob demanda e retorna a classe HTML."""
    global _weasyprint_HTML
    if _weasyprint_HTML is None:
        try:
            from weasyprint import HTML
            _weasyprint_HTML = HTML
        except (ImportError, OSError) as e:
            raise RuntimeError(
                "WeasyPrint nao esta disponivel neste ambiente. "
                "Certifique-se de que as dependencias de sistema estao instaladas "
                "(libpango, libcairo, libgdk-pixbuf). "
                "Consulte: https://doc.courtbouillon.org/weasyprint/stable/first_steps.html\n"
                f"Erro original: {e}"
            ) from e
    return _weasyprint_HTML

# ---------------------------------------------------------------------------
# CSS profissional embutido — tipografia limpa e layout corporativo
# ---------------------------------------------------------------------------
_BASE_CSS = """
@page {{
    size: {page_size};
    margin: {margin_top} {margin_right} {margin_bottom} {margin_left};
    @top-center {{
        content: "{header_text}";
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size: 9px;
        color: #888888;
    }}
    @bottom-center {{
        content: "{footer_text}";
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size: 9px;
        color: #888888;
    }}
    @bottom-right {{
        content: counter(page) " / " counter(pages);
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size: 9px;
        color: #888888;
    }}
}}

body {{
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #1a1a1a;
    max-width: 100%;
}}

h1 {{
    font-size: 22pt;
    font-weight: 700;
    color: #1F4E79;
    border-bottom: 2px solid #1F4E79;
    padding-bottom: 6px;
    margin-top: 24px;
    margin-bottom: 12px;
}}

h2 {{
    font-size: 16pt;
    font-weight: 600;
    color: #2E86AB;
    margin-top: 20px;
    margin-bottom: 8px;
}}

h3 {{
    font-size: 13pt;
    font-weight: 600;
    color: #444444;
    margin-top: 16px;
    margin-bottom: 6px;
}}

p {{
    margin-bottom: 10px;
    text-align: justify;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 10pt;
}}

th {{
    background-color: #1F4E79;
    color: #ffffff;
    font-weight: 600;
    text-align: left;
    padding: 8px 10px;
}}

td {{
    padding: 6px 10px;
    border-bottom: 1px solid #dee2e6;
}}

tr:nth-child(even) td {{
    background-color: #f8f9fa;
}}

code {{
    background-color: #f4f4f4;
    padding: 2px 5px;
    border-radius: 3px;
    font-family: "Courier New", Courier, monospace;
    font-size: 10pt;
}}

pre {{
    background-color: #f4f4f4;
    padding: 12px;
    border-radius: 4px;
    overflow-x: auto;
    font-size: 9pt;
    line-height: 1.4;
}}

blockquote {{
    border-left: 4px solid #2E86AB;
    margin: 12px 0;
    padding: 8px 16px;
    color: #555555;
    background-color: #f0f7fb;
}}

ul, ol {{
    margin-bottom: 10px;
    padding-left: 24px;
}}

li {{
    margin-bottom: 4px;
}}

a {{
    color: #2E86AB;
    text-decoration: none;
}}

hr {{
    border: none;
    border-top: 1px solid #cccccc;
    margin: 20px 0;
}}
"""


def _safe_output_path(path: str) -> str:
    """Gera um caminho seguro, sem sobrescrever arquivo existente."""
    if not os.path.exists(path):
        return path
    base, ext = os.path.splitext(path)
    counter = 1
    while os.path.exists(f"{base}_{counter}{ext}"):
        counter += 1
    return f"{base}_{counter}{ext}"


def _build_css(config: Optional[Dict[str, Any]] = None) -> str:
    """Monta o CSS final com base na configuracao fornecida."""
    config = config or {}
    page_size = config.get("page_size", "A4")
    margins = config.get("margins", {})
    header_text = config.get("header_text", "")
    footer_text = config.get("footer_text", "")

    return _BASE_CSS.format(
        page_size=page_size,
        margin_top=margins.get("top", "20mm"),
        margin_right=margins.get("right", "15mm"),
        margin_bottom=margins.get("bottom", "20mm"),
        margin_left=margins.get("left", "15mm"),
        header_text=header_text,
        footer_text=footer_text,
    )


def build_pdf_from_html(
    html_string: str,
    output_path: str,
    config: Optional[Dict[str, Any]] = None,
) -> str:
    """
    Gera um PDF profissional a partir de uma string HTML.

    Parametros
    ----------
    html_string : str
        Conteudo HTML a ser convertido em PDF.
    output_path : str
        Caminho do arquivo PDF de saida.
    config : dict, opcional
        Opcoes de configuracao:
            - page_size   : str  — 'A4' | 'Letter' (padrao: 'A4')
            - margins     : dict — {'top': '20mm', 'right': '15mm', 'bottom': '20mm', 'left': '15mm'}
            - header_text : str  — texto no cabecalho de cada pagina
            - footer_text : str  — texto no rodape de cada pagina

    Retorno
    -------
    str
        Caminho absoluto do arquivo PDF gerado.
    """
    if not html_string or not html_string.strip():
        raise ValueError("O conteudo HTML esta vazio. Nenhum PDF gerado.")

    output_path = _safe_output_path(output_path)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    css = _build_css(config)

    full_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <style>{css}</style>
</head>
<body>
{html_string}
</body>
</html>"""

    HTML = _get_weasyprint_html()
    HTML(string=full_html).write_pdf(output_path)
    return os.path.abspath(output_path)


def build_pdf_from_markdown(
    md_string: str,
    output_path: str,
    config: Optional[Dict[str, Any]] = None,
) -> str:
    """
    Converte uma string Markdown em HTML e gera um PDF profissional.

    Parametros
    ----------
    md_string : str
        Conteudo Markdown a ser convertido.
    output_path : str
        Caminho do arquivo PDF de saida.
    config : dict, opcional
        Mesmas opcoes de build_pdf_from_html.

    Retorno
    -------
    str
        Caminho absoluto do arquivo PDF gerado.
    """
    if not md_string or not md_string.strip():
        raise ValueError("O conteudo Markdown esta vazio. Nenhum PDF gerado.")

    html_body = markdown.markdown(
        md_string,
        extensions=["tables", "fenced_code", "codehilite", "toc", "nl2br"],
    )

    return build_pdf_from_html(html_body, output_path, config)
