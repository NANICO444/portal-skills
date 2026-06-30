"""
chart_builder.py — Ultra Prompt v6.1
Construtor profissional de graficos e dashboards.

Exports:
    - build_single_chart(data, chart_type, config) -> str
    - build_dashboard(charts_config, output_path) -> str

Dependencias: matplotlib, seaborn
"""

__all__ = ["build_single_chart", "build_dashboard"]

import os
import math
import datetime
from typing import Any, Dict, List, Optional, Tuple

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.ticker as ticker  # noqa: E402
import seaborn as sns  # noqa: E402
import numpy as np  # noqa: E402


# ---------------------------------------------------------------------------
# Paleta profissional padrao
# ---------------------------------------------------------------------------
PALETTE = ["#1F4E79", "#2E86AB", "#A23B72", "#F18F01", "#C73E1D"]

# Configuracao global do matplotlib para visual limpo
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica Neue", "Arial", "DejaVu Sans"],
    "font.size": 11,
    "axes.titlesize": 14,
    "axes.titleweight": "bold",
    "axes.labelsize": 12,
    "axes.edgecolor": "#cccccc",
    "axes.linewidth": 0.8,
    "xtick.color": "#555555",
    "ytick.color": "#555555",
    "legend.fontsize": 10,
    "legend.framealpha": 0.9,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.dpi": 150,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.3,
})


def _safe_output_path(path: str) -> str:
    """Gera um caminho seguro, sem sobrescrever arquivo existente."""
    if not os.path.exists(path):
        return path
    base, ext = os.path.splitext(path)
    counter = 1
    while os.path.exists(f"{base}_{counter}{ext}"):
        counter += 1
    return f"{base}_{counter}{ext}"


def _clean_spines(ax: plt.Axes) -> None:
    """Remove spines superiores e direitos para visual limpo."""
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#cccccc")
    ax.spines["bottom"].set_color("#cccccc")
    ax.tick_params(axis="both", which="both", length=0)
    ax.grid(axis="y", linestyle="--", alpha=0.3, color="#888888")


def _apply_common_config(ax: plt.Axes, config: Dict[str, Any]) -> None:
    """Aplica titulo, labels e legenda com base na config."""
    if config.get("title"):
        ax.set_title(config["title"], pad=12)
    if config.get("xlabel"):
        ax.set_xlabel(config["xlabel"])
    if config.get("ylabel"):
        ax.set_ylabel(config["ylabel"])


def _plot_bar(ax: plt.Axes, data: Dict[str, Any], config: Dict[str, Any]) -> None:
    """Renderiza grafico de barras."""
    labels = data.get("labels", [])
    values = data.get("values", [])
    colors = config.get("colors", PALETTE)

    bar_colors = [colors[i % len(colors)] for i in range(len(labels))]
    bars = ax.bar(labels, values, color=bar_colors, edgecolor="white", linewidth=0.5)

    # Valores sobre as barras
    for bar, val in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{val:,.1f}" if isinstance(val, float) else str(val),
            ha="center",
            va="bottom",
            fontsize=9,
            color="#333333",
        )
    _clean_spines(ax)


def _plot_line(ax: plt.Axes, data: Dict[str, Any], config: Dict[str, Any]) -> None:
    """Renderiza grafico de linha. Suporta multiplas series."""
    colors = config.get("colors", PALETTE)

    # Suporte a multiplas series: data['series'] = [{'name': ..., 'x': ..., 'y': ...}, ...]
    if "series" in data:
        for i, s in enumerate(data["series"]):
            ax.plot(
                s["x"], s["y"],
                marker="o", markersize=4,
                color=colors[i % len(colors)],
                label=s.get("name", f"Serie {i+1}"),
                linewidth=2,
            )
    else:
        x = data.get("x", list(range(len(data.get("y", [])))))
        y = data.get("y", [])
        ax.plot(x, y, marker="o", markersize=4, color=colors[0], linewidth=2, label=config.get("title", ""))

    ax.legend(loc="best")
    _clean_spines(ax)


def _plot_pie(ax: plt.Axes, data: Dict[str, Any], config: Dict[str, Any]) -> None:
    """Renderiza grafico de pizza."""
    labels = data.get("labels", [])
    values = data.get("values", [])
    colors = config.get("colors", PALETTE)

    pie_colors = [colors[i % len(colors)] for i in range(len(labels))]

    wedges, texts, autotexts = ax.pie(
        values,
        labels=labels,
        colors=pie_colors,
        autopct="%1.1f%%",
        startangle=140,
        pctdistance=0.8,
        wedgeprops={"edgecolor": "white", "linewidth": 1.5},
    )
    for text in autotexts:
        text.set_fontsize(9)
        text.set_color("#333333")
    ax.set_aspect("equal")


def _plot_heatmap(ax: plt.Axes, data: Dict[str, Any], config: Dict[str, Any]) -> None:
    """Renderiza mapa de calor usando seaborn."""
    matrix = data.get("matrix", [])
    x_labels = data.get("x_labels", None)
    y_labels = data.get("y_labels", None)

    arr = np.array(matrix)
    sns.heatmap(
        arr,
        ax=ax,
        annot=True,
        fmt=".1f",
        cmap="YlOrRd",
        linewidths=0.5,
        linecolor="white",
        xticklabels=x_labels if x_labels else "auto",
        yticklabels=y_labels if y_labels else "auto",
        cbar_kws={"shrink": 0.8},
    )


# Mapeamento de tipos de grafico para funcoes de plotagem
_PLOT_FUNCTIONS = {
    "bar": _plot_bar,
    "line": _plot_line,
    "pie": _plot_pie,
    "heatmap": _plot_heatmap,
}


def build_single_chart(
    data: Dict[str, Any],
    chart_type: str,
    config: Optional[Dict[str, Any]] = None,
) -> str:
    """
    Gera um unico grafico profissional e salva como imagem PNG.

    Parametros
    ----------
    data : dict
        Dados do grafico. Estrutura depende do tipo:
        - bar/pie : {'labels': [...], 'values': [...]}
        - line    : {'x': [...], 'y': [...]} ou {'series': [{'name': ..., 'x': ..., 'y': ...}, ...]}
        - heatmap : {'matrix': [[...]], 'x_labels': [...], 'y_labels': [...]}
    chart_type : str
        Tipo do grafico: 'bar' | 'line' | 'pie' | 'heatmap'
    config : dict, opcional
        Opcoes de configuracao:
            - title       : str        — titulo do grafico
            - xlabel      : str        — rotulo do eixo X
            - ylabel      : str        — rotulo do eixo Y
            - colors      : list[str]  — lista de cores hex
            - figsize     : tuple      — dimensoes (largura, altura) em polegadas
            - output_path : str        — caminho do arquivo de saida

    Retorno
    -------
    str
        Caminho absoluto da imagem PNG gerada.
    """
    if chart_type not in _PLOT_FUNCTIONS:
        raise ValueError(
            f"Tipo de grafico '{chart_type}' invalido. "
            f"Opcoes: {', '.join(_PLOT_FUNCTIONS.keys())}"
        )

    config = config or {}
    figsize = config.get("figsize", (10, 6))

    fig, ax = plt.subplots(figsize=figsize)

    # Plotar
    _PLOT_FUNCTIONS[chart_type](ax, data, config)
    _apply_common_config(ax, config)

    # Caminho de saida
    default_name = f"chart_{chart_type}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    output_path = config.get("output_path", os.path.join("/home/vercel-sandbox", default_name))
    output_path = _safe_output_path(output_path)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return os.path.abspath(output_path)


def build_dashboard(
    charts_config: List[Dict[str, Any]],
    output_path: str,
) -> str:
    """
    Gera um dashboard com multiplos graficos organizados em grid.

    Parametros
    ----------
    charts_config : list[dict]
        Lista de configuracoes de graficos. Cada item deve conter:
            - data       : dict — dados do grafico (mesma estrutura de build_single_chart)
            - chart_type : str  — 'bar' | 'line' | 'pie' | 'heatmap'
            - config     : dict — configuracao individual (title, xlabel, ylabel, colors)
    output_path : str
        Caminho do arquivo PNG de saida.

    Retorno
    -------
    str
        Caminho absoluto da imagem PNG gerada.
    """
    if not charts_config:
        raise ValueError("A lista de graficos esta vazia. Nenhum dashboard gerado.")

    n = len(charts_config)
    cols = min(n, 2)
    rows = math.ceil(n / cols)

    fig, axes = plt.subplots(
        rows, cols,
        figsize=(10 * cols, 6 * rows),
        squeeze=False,
    )

    for idx, chart_def in enumerate(charts_config):
        row = idx // cols
        col = idx % cols
        ax = axes[row][col]

        chart_type = chart_def.get("chart_type", "bar")
        data = chart_def.get("data", {})
        cfg = chart_def.get("config", {})

        if chart_type not in _PLOT_FUNCTIONS:
            ax.text(0.5, 0.5, f"Tipo invalido: {chart_type}", ha="center", va="center")
            continue

        _PLOT_FUNCTIONS[chart_type](ax, data, cfg)
        _apply_common_config(ax, cfg)

    # Ocultar eixos vazios
    for idx in range(n, rows * cols):
        row = idx // cols
        col = idx % cols
        axes[row][col].set_visible(False)

    fig.suptitle("Dashboard", fontsize=18, fontweight="bold", color="#1F4E79", y=1.01)
    fig.tight_layout()

    output_path = _safe_output_path(output_path)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    fig.savefig(output_path, dpi=150)
    plt.close(fig)

    return os.path.abspath(output_path)
