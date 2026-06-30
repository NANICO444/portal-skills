#!/usr/bin/env python3
"""
token-budget-advisor — helper de estimativa e recomendação.

Estima tokens (heurística grosseira ~4 chars/token) e recomenda modelo
(MODELO_A/Pro pra difícil, MODELO_B/Flash pra simples) + alertas de orçamento.

NÃO é um contador exato nem uma calculadora de custo. Serve pra ordem de
grandeza e roteamento de modelo. Model-agnóstico: não chama nenhuma API.

Uso:
    python implementation.py --chars 48000 --complexity simples
    python implementation.py --file caminho.txt --complexity dificil
    python implementation.py --chars 600000 --complexity dificil --output longa
"""

import argparse
import sys

# Janela de contexto dos modelos do sistema (DeepSeek V4 Pro/Flash) — 1M tokens.
# Ver 05_OUTPUT/_DEEPSEEK_BASICS.md. [VALIDAR: confirmar se muda no Hermes runtime]
CONTEXT_WINDOW = 1_000_000
CHARS_PER_TOKEN = 4  # heurística grosseira; varia por idioma/conteúdo

MODELO_A = "MODELO_A/Pro (DeepSeek V4 Pro)"
MODELO_B = "MODELO_B/Flash (DeepSeek V4 Flash)"


def estimar_tokens(chars: int) -> int:
    """Estimativa grosseira de tokens a partir de contagem de caracteres."""
    return max(0, chars // CHARS_PER_TOKEN)


def recomendar_modelo(complexidade: str) -> tuple[str, str]:
    """Recomenda modelo por papel, não por preço (preço é volátil)."""
    if complexidade == "dificil":
        return MODELO_A, "raciocínio profundo / código não trivial / síntese complexa"
    return MODELO_B, "tarefa simples/repetitiva — mais rápido e barato"


def montar_alertas(tokens: int, pct: float, output: str, complexidade: str) -> list[str]:
    alertas = []
    if pct >= 50:
        alertas.append(
            f"entrada estimada usa ~{pct:.0f}% da janela — considere dividir/paginar a tarefa"
        )
    if output == "longa":
        alertas.append(
            "saída longa esperada — garanta max_tokens adequado pra não truncar no meio"
        )
    if pct >= 30 or output == "longa":
        alertas.append(
            "sessão pode crescer — rode context-snapshot ANTES (baseline §15.3 #14)"
        )
    if complexidade == "simples" and tokens > 200_000:
        alertas.append(
            "tarefa simples mas contexto grande — confirme se todo esse contexto é necessário"
        )
    return alertas or ["nenhum"]


def main() -> int:
    p = argparse.ArgumentParser(description="Token budget advisor (estimativa grosseira).")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--chars", type=int, help="número de caracteres do contexto estimado")
    g.add_argument("--file", type=str, help="arquivo para medir o tamanho em caracteres")
    p.add_argument(
        "--complexity",
        choices=["simples", "dificil"],
        required=True,
        help="complexidade da tarefa (simples → Flash, dificil → Pro)",
    )
    p.add_argument(
        "--output",
        choices=["curta", "media", "longa"],
        default="media",
        help="tamanho esperado da saída",
    )
    args = p.parse_args()

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8", errors="replace") as fh:
                chars = len(fh.read())
        except OSError as e:
            print(f"erro ao ler arquivo: {e}", file=sys.stderr)
            return 1
    else:
        chars = args.chars

    tokens = estimar_tokens(chars)
    pct = (tokens / CONTEXT_WINDOW) * 100
    modelo, motivo = recomendar_modelo(args.complexity)
    alertas = montar_alertas(tokens, pct, args.output, args.complexity)

    print("ORÇAMENTO SUGERIDO")
    print(f"- Complexidade: {args.complexity}")
    print(f"- Modelo recomendado: {modelo} — {motivo}")
    print(f"- Entrada estimada: ~{tokens:,} tokens (~{pct:.1f}% da janela de 1M)")
    print(f"- Saída esperada: {args.output}")
    print(f"- Alerta: {'; '.join(alertas)}")
    print()
    print("(estimativa grosseira ~4 chars/token; conselho, não imposição)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
