#!/usr/bin/env python3
"""
skills_loader.py — Roteador de skills para agentes IA
Uso: python3 skills_loader.py "abrir empresa TI simples nacional"
     python3 skills_loader.py "calcular viabilidade financeira startup"
     python3 skills_loader.py --load brazil_tax_regulatory
     python3 skills_loader.py --list

Token economy: agente roda este script (50 tokens output) ao inves de
carregar todo o repositorio (56.000 tokens).
"""

import sys
import os
import urllib.request

GITHUB_RAW = "https://raw.githubusercontent.com/Joehott/skills/main/skills/business"

# ── MAPA DE SKILLS ──────────────────────────────────────

SKILLS = {
    "brazil_tax_regulatory": {
        "file": "brazil_tax_regulatory.md",
        "tokens": 3967,
        "desc": "Regimes tributarios, tipos de empresa, armadilhas, holding",
        "keywords": ["regime", "tributar", "simples", "presumido", "lucro real", "mei",
                     "empresa", "ltda", "sa", "cnpj", "abrir", "abertura", "holding",
                     "armadilha", "dividendo", "pro-labore", "prolabore"],
    },
    "brazil_tax_complete": {
        "file": "brazil_tax_complete.md",
        "tokens": 8243,
        "desc": "6 regimes completos: MEI, Simples, Presumido, Real, SA, Capital Estrangeiro",
        "keywords": ["aliquota", "mei", "simples nacional", "anexo", "fator-r",
                     "irpj", "csll", "pis", "cofins", "lalur", "cvm", "b3",
                     "capital estrangeiro", "transfer pricing", "todas as aliquotas",
                     "referencia", "comparar regimes"],
    },
    "brazil_tax_obligations_calendar": {
        "file": "brazil_tax_obligations_calendar.md",
        "tokens": 4727,
        "desc": "Calendario fiscal 2026, prazos, multas, sistemas obrigatorios",
        "keywords": ["prazo", "vencimento", "calendario", "das", "fgts", "dctfweb",
                     "ecd", "ecf", "defis", "dasn", "multa", "penalidade",
                     "obrigacao", "sistema", "esocial", "sped", "2026"],
    },
    "brazil_tax_special_regimes": {
        "file": "brazil_tax_special_regimes.md",
        "tokens": 5409,
        "desc": "RET, REIDI, Lei do Bem, Zona Franca, RECAP, PADIS, Transacao Tributaria",
        "keywords": ["ret", "reidi", "lei do bem", "zona franca", "manaus", "zfm",
                     "recap", "padis", "transacao tributaria", "pert", "parcelamento",
                     "divida fiscal", "incentivo", "beneficio fiscal", "ipi zero",
                     "p&d", "pd", "pesquisa desenvolvimento", "infraestrutura",
                     "imobiliaria", "incorporadora", "exportador", "semicondutor"],
    },
    "brazil_tax_reform_2026_2032": {
        "file": "brazil_tax_reform_2026_2032.md",
        "tokens": 5481,
        "desc": "Reforma Tributaria: CBS, IBS, IS, IRPF Minimo, cronograma 2026-2033",
        "keywords": ["reforma tributaria", "cbs", "ibs", "imposto seletivo",
                     "irpf minimo", "dividendo 10%", "split payment", "destino",
                     "2027", "2028", "2029", "2033", "transicao", "lc 214",
                     "ec 132", "pl 1087", "novo sistema", "reforma 2026"],
    },
    "brazil_tax_individual_optimization": {
        "file": "brazil_tax_individual_optimization.md",
        "tokens": 5499,
        "desc": "Pro-labore otimo, PGBL/VGBL, IRPF Minimo, ITCMD, holding familiar",
        "keywords": ["pro-labore", "prolabore", "dividendo", "pgbl", "vgbl",
                     "previdencia privada", "irpf", "irpf minimo", "pessoa fisica",
                     "socio", "itcmd", "heranca", "doacao", "sucessao",
                     "holding familiar", "aposentadoria", "otimizacao fiscal",
                     "quanto retirar", "remuneracao socio"],
    },
    "business_analysis": {
        "file": "business_analysis.md",
        "tokens": 2313,
        "desc": "SWOT, Porter 5 Forcas, PESTEL, BCG, VRIO, Cadeia de Valor",
        "keywords": ["swot", "porter", "5 forcas", "pestel", "bcg", "vrio",
                     "cadeia de valor", "analise", "empresa existente",
                     "concorrencia", "mercado", "posicionamento", "diagnostico"],
    },
    "business_idea_validation": {
        "file": "business_idea_validation.md",
        "tokens": 3082,
        "desc": "Lean Canvas, BMC, PMF, TAM/SAM/SOM, JTBD, Unit Economics, MVP",
        "keywords": ["lean canvas", "bmc", "pmf", "product market fit",
                     "tam", "sam", "som", "mercado", "validar", "validacao",
                     "ideia", "mvp", "experimento", "jtbd", "jobs to be done",
                     "cac", "ltv", "unit economics", "startup", "modelo de negocio"],
    },
    "business_plan_creation": {
        "file": "business_plan_creation.md",
        "tokens": 3189,
        "desc": "Plano de negocios 8 secoes completas + Pitch Deck 10 slides",
        "keywords": ["plano de negocio", "business plan", "pitch", "pitch deck",
                     "sumario executivo", "estrutura", "plano completo",
                     "banco", "financiamento", "bndes", "investidor"],
    },
    "business_viability_calculation": {
        "file": "business_viability_calculation.md",
        "tokens": 3401,
        "desc": "VPL, TIR, Payback, Break-even, Valuation, Projecao 3 anos",
        "keywords": ["vpl", "tir", "payback", "break-even", "breakeven",
                     "viabilidade", "retorno", "investimento", "valuation",
                     "fluxo de caixa", "dre", "projecao", "cenario",
                     "tma", "custo de oportunidade", "vale a pena"],
    },
}

# ── ROTEADOR ────────────────────────────────────────────

def route(query: str) -> list[str]:
    """Retorna lista de skills recomendadas para a query."""
    q = query.lower()
    scores: dict[str, int] = {}

    for skill_id, skill in SKILLS.items():
        score = 0
        for kw in skill["keywords"]:
            if kw in q:
                # Palavras-chave exatas valem mais
                score += 2 if len(kw) > 8 else 1
        if score > 0:
            scores[skill_id] = score

    # Se nao encontrou nada, sugerir os de negocios
    if not scores:
        return ["business_analysis", "business_viability_calculation"]

    # Ordenar por score e retornar top 3
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [skill_id for skill_id, _ in ranked[:3]]


# ── CARREGADOR ──────────────────────────────────────────

def load_skill(skill_id: str, local_dir: str = None) -> str:
    """Carrega o conteudo de uma skill (local ou GitHub)."""
    skill = SKILLS.get(skill_id)
    if not skill:
        # Tentar como nome de arquivo direto
        fname = skill_id if skill_id.endswith('.md') else skill_id + '.md'
        skill = {"file": fname, "tokens": 0, "desc": ""}

    fname = skill["file"]

    # Tentar local primeiro
    if local_dir:
        path = os.path.join(local_dir, fname)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()

    # Tentar mesmo diretorio do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, fname)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    # Fallback: GitHub raw
    url = f"{GITHUB_RAW}/{fname}"
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'skills-loader/1.0')
        resp = urllib.request.urlopen(req, timeout=10)
        return resp.read().decode('utf-8')
    except Exception as e:
        return f"ERRO ao carregar {fname}: {e}\nURL tentada: {url}"


# ── INTERFACE CLI ────────────────────────────────────────

def main():
    args = sys.argv[1:]

    if not args or "--help" in args:
        print(__doc__)
        print("\nComandos:")
        print("  python3 skills_loader.py \"sua tarefa aqui\"   → recomenda skills")
        print("  python3 skills_loader.py --load <skill_id>   → imprime conteudo da skill")
        print("  python3 skills_loader.py --list              → lista todas as skills")
        print("  python3 skills_loader.py --fetch <skill_id>  → baixa do GitHub")
        return

    if "--list" in args:
        print(f"\n{'SKILL ID':<40} {'TOKENS':>7}  DESCRICAO")
        print("-" * 80)
        for skill_id, skill in SKILLS.items():
            print(f"{skill_id:<40} {skill['tokens']:>7}  {skill['desc']}")
        total = sum(s["tokens"] for s in SKILLS.values())
        print(f"\n{'TOTAL (se carregar tudo)':<40} {total:>7}")
        return

    if "--load" in args:
        idx = args.index("--load")
        skill_id = args[idx + 1] if idx + 1 < len(args) else None
        if not skill_id:
            print("Informe o skill_id apos --load")
            return
        content = load_skill(skill_id)
        print(content)
        return

    if "--fetch" in args:
        idx = args.index("--fetch")
        skill_id = args[idx + 1] if idx + 1 < len(args) else None
        if not skill_id:
            print("Informe o skill_id apos --fetch")
            return
        skill = SKILLS.get(skill_id, {"file": skill_id + ".md"})
        url = f"{GITHUB_RAW}/{skill['file']}"
        print(f"Buscando: {url}")
        content = load_skill(skill_id)
        fname = skill.get("file", skill_id + ".md")
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Salvo em: {fname}")
        return

    # Modo roteador: query livre
    query = " ".join(args)
    recommended = route(query)

    print(f"\nQuery: \"{query}\"")
    print(f"\nSkills recomendadas ({len(recommended)}):\n")

    total_tokens = 0
    for i, skill_id in enumerate(recommended, 1):
        skill = SKILLS[skill_id]
        total_tokens += skill["tokens"]
        print(f"  {i}. {skill['file']}")
        print(f"     {skill['tokens']} tokens | {skill['desc']}")
        print(f"     Carregar: python3 skills_loader.py --load {skill_id}")
        print()

    print(f"Total estimado: {total_tokens} tokens")
    print(f"Economia vs carregar tudo: {56000 - total_tokens:,} tokens")

    # Aviso se CNAE foi mencionado
    if any(kw in query.lower() for kw in ["cnae", "atividade", "codigo", "cbo"]):
        print("\n⚡ CNAE detectado na query — use o script diretamente:")
        print("   python3 brazil_cnae_database.py --search \"<sua atividade>\"")
        print("   python3 brazil_cnae_database.py <codigo_cnae>")


if __name__ == "__main__":
    main()
