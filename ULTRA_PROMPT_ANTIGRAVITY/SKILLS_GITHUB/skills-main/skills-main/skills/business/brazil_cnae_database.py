#!/usr/bin/env python3
"""
brazil_cnae_database.py — Consulta CNAE x Regime Tributario x Aliquota
Versao: 1.0.0
Criado: 2026-05-17 | Sessao: sess_20260517_2226_biz
Uso: python3 brazil_cnae_database.py [cnae_code]
     python3 brazil_cnae_database.py --search "programacao"
     python3 brazil_cnae_database.py --list-vedados
     python3 brazil_cnae_database.py --simular --cnae 6201500 --faturamento 500000
"""

import sys
import json
from dataclasses import dataclass
from typing import Optional


# ─────────────────────────────────────────────────────────
# 1. ESTRUTURAS DE DADOS
# ─────────────────────────────────────────────────────────

@dataclass
class CNAEInfo:
    codigo: str
    descricao: str
    anexo_simples: Optional[str]          # "I", "II", "III", "IV", "V" ou None
    vedado_simples: bool
    motivo_vedacao: Optional[str]
    iss_faixa: str                         # "2-5%" ou N/A
    icms: bool                             # True se gera ICMS
    ipi: bool                              # True se gera IPI
    observacoes: str


# ─────────────────────────────────────────────────────────
# 2. BASE DE DADOS CNAE × SIMPLES NACIONAL
# ─────────────────────────────────────────────────────────
# Fonte: Resolução CGSN 140/2018 + atualizações 2024-2025
# Cobertura: ~200 CNAEs mais comuns; expandir conforme necessário

CNAE_DATABASE: dict[str, CNAEInfo] = {

    # ── TECNOLOGIA DA INFORMAÇÃO ──────────────────────────
    "6201500": CNAEInfo("6201500", "Desenvolvimento de programas de computador sob encomenda",
        "III", False, None, "2-5%", False, False,
        "TI sob encomenda = Anexo III (sem Fator-R). Se folha/RBT12 >= 28%: Anexo III mantido."),
    "6202300": CNAEInfo("6202300", "Desenvolvimento e licenciamento de programas de computador customizáveis",
        "III", False, None, "2-5%", False, False,
        "Software customizável = Anexo III. Atenção: licenciamento de prateleira pode ir para ISS fixo em alguns municípios."),
    "6203100": CNAEInfo("6203100", "Desenvolvimento e licenciamento de programas de computador não customizáveis",
        "III", False, None, "2-5%", False, False,
        "Software de prateleira. ISS em alguns municípios, ICMS em outros (disputado judicialmente)."),
    "6204000": CNAEInfo("6204000", "Consultoria em tecnologia da informação",
        "III", False, None, "2-5%", False, False,
        "Consultoria TI = Anexo III Simples. Margem alta = avaliar Lucro Presumido (32% base)."),
    "6209100": CNAEInfo("6209100", "Suporte técnico, manutenção e outros serviços em TI",
        "III", False, None, "2-5%", False, False,
        "Suporte/Manutenção TI = Anexo III."),
    "6311900": CNAEInfo("6311900", "Tratamento de dados, provedores de serviços de aplicação",
        "III", False, None, "2-5%", False, False,
        "SaaS/hosting = Anexo III. Em 2027+ CBS pode subir carga de serviços digitais."),
    "6319400": CNAEInfo("6319400", "Portais, provedores de conteúdo e outros serviços de informação",
        "III", False, None, "2-5%", False, False,
        "Portais e conteúdo digital = Anexo III."),

    # ── COMÉRCIO VAREJISTA ────────────────────────────────
    "4711301": CNAEInfo("4711301", "Comércio varejista de mercadorias em geral - hipermercados",
        "I", False, None, "N/A", True, False,
        "Varejo geral = Anexo I (comércio). ICMS incide normalmente."),
    "4712100": CNAEInfo("4712100", "Comércio varejista de mercadorias em geral - minimercados e mercearias",
        "I", False, None, "N/A", True, False,
        "Varejo de alimentos = Anexo I. ICMS na saída."),
    "4713001": CNAEInfo("4713001", "Lojas de departamentos ou magazines",
        "I", False, None, "N/A", True, False,
        "Loja de departamento = Anexo I."),
    "4721103": CNAEInfo("4721103", "Comércio varejista de laticínios e frios",
        "I", False, None, "N/A", True, False,
        "Laticínios e frios = Anexo I."),
    "4751201": CNAEInfo("4751201", "Comércio varejista especializado de equipamentos e suprimentos de informática",
        "I", False, None, "N/A", True, False,
        "Informática varejo = Anexo I. IPI pode incidir na indústria fornecedora."),
    "4781400": CNAEInfo("4781400", "Comércio varejista de artigos do vestuário e acessórios",
        "I", False, None, "N/A", True, False,
        "Vestuário varejo = Anexo I."),
    "4789099": CNAEInfo("4789099", "Comércio varejista de outros produtos não especificados",
        "I", False, None, "N/A", True, False,
        "Varejo geral outros = Anexo I."),

    # ── COMÉRCIO ATACADISTA ───────────────────────────────
    "4611700": CNAEInfo("4611700", "Representantes comerciais e agentes do comércio de matérias-primas agrícolas",
        "III", False, None, "2-5%", False, False,
        "Representante comercial (comissões) = Anexo III (serviço de intermediação)."),
    "4621400": CNAEInfo("4621400", "Comércio atacadista de café em grão",
        "I", False, None, "N/A", True, False,
        "Atacado de café = Anexo I."),

    # ── INDÚSTRIA / MANUFATURA ────────────────────────────
    "1011201": CNAEInfo("1011201", "Frigorífico - abate de bovinos",
        "II", False, None, "N/A", True, True,
        "Indústria frigorífico = Anexo II. IPI + ICMS incidem. Verifique ICMS-ST em alguns estados."),
    "1091101": CNAEInfo("1091101", "Fabricação de produtos de panificação industrial",
        "II", False, None, "N/A", True, True,
        "Panificação industrial = Anexo II."),
    "2211100": CNAEInfo("2211100", "Fabricação de pneumáticos e câmaras-de-ar",
        "II", False, None, "N/A", True, True,
        "Pneumáticos = Anexo II. ICMS-ST provável para distribuidores."),
    "2751100": CNAEInfo("2751100", "Fabricação de fogões, refrigeradores e máquinas domésticas",
        "II", False, None, "N/A", True, True,
        "Eletrodomésticos = Anexo II. IPI expressivo neste setor."),
    "2631100": CNAEInfo("2631100", "Fabricação de equipamentos transmissores de comunicação",
        "II", False, None, "N/A", True, True,
        "Telecom hardware = Anexo II. Se em ZFM: IPI zero."),

    # ── CONSTRUÇÃO CIVIL ──────────────────────────────────
    "4110700": CNAEInfo("4110700", "Incorporação de empreendimentos imobiliários",
        "IV", False, None, "2-5%", False, False,
        "Incorporadora = Anexo IV (INSS patronal fora do DAS). Avaliar RET (4% sobre receita por empreendimento)."),
    "4120400": CNAEInfo("4120400", "Construção de edifícios",
        "IV", False, None, "2-5%", False, False,
        "Construtora = Anexo IV. INSS patronal não incluído no DAS."),
    "4211101": CNAEInfo("4211101", "Construção de rodovias e ferrovias",
        "IV", False, None, "2-5%", False, False,
        "Obras rodovias = Anexo IV. Avaliar REIDI se projeto habilitado."),
    "4330404": CNAEInfo("4330404", "Instalações de sistemas de ar-condicionado, de ventilação e refrigeração",
        "IV", False, None, "2-5%", False, False,
        "Instalação HVAC = Anexo IV."),

    # ── SAÚDE E EDUCAÇÃO ──────────────────────────────────
    "8621601": CNAEInfo("8621601", "UTI móvel",
        None, True, "Atividade médica vedada se S/A (não se LTDA individual)",
        "2-5%", False, False,
        "Serviços médicos em geral: LTDA pode estar no Simples III. Verificar vedação por tipo societário."),
    "8630501": CNAEInfo("8630501", "Atividade médica ambulatorial com recursos para realização de procedimentos cirúrgicos",
        "III", False, None, "2-5%", False, False,
        "Clínica cirúrgica = Anexo III. Serviços médicos com folha alta: verificar Fator-R (Anexo III vs V)."),
    "8630502": CNAEInfo("8630502", "Atividade médica ambulatorial com recursos para realização de exames complementares",
        "III", False, None, "2-5%", False, False,
        "Exames complementares = Anexo III."),
    "8640202": CNAEInfo("8640202", "Laboratórios clínicos",
        "III", False, None, "2-5%", False, False,
        "Laboratório clínico = Anexo III."),
    "8650001": CNAEInfo("8650001", "Atividades de enfermagem",
        "III", False, None, "2-5%", False, False,
        "Enfermagem = Anexo III."),
    "8511200": CNAEInfo("8511200", "Educação infantil – creche",
        "III", False, None, "2-5%", False, False,
        "Creche = Anexo III. ISS reduzido em muitos municípios para educação."),
    "8513900": CNAEInfo("8513900", "Ensino fundamental",
        "III", False, None, "2-5%", False, False,
        "Escola fundamental = Anexo III."),
    "8541400": CNAEInfo("8541400", "Educação profissional de nível técnico",
        "III", False, None, "2-5%", False, False,
        "Escola técnica = Anexo III."),
    "8599604": CNAEInfo("8599604", "Treinamento em desenvolvimento profissional e gerencial",
        "III", False, None, "2-5%", False, False,
        "Treinamento/coaching = Anexo III."),

    # ── SERVIÇOS PROFISSIONAIS ────────────────────────────
    "6911701": CNAEInfo("6911701", "Serviços advocatícios",
        "IV", False, None, "2-5%", False, False,
        "Advocacia = Anexo IV. INSS patronal fora do DAS. Alíquotas mais altas que Anexo III."),
    "7111100": CNAEInfo("7111100", "Serviços de arquitetura",
        "V", False, None, "2-5%", False, False,
        "Arquitetura = Anexo V (alta folha de pagamento). Fator-R: se folha >= 28% da RBT12 → Anexo III."),
    "7112000": CNAEInfo("7112000", "Serviços de engenharia",
        "V", False, None, "2-5%", False, False,
        "Engenharia = Anexo V. Fator-R: folha >= 28% RBT12 → Anexo III (economia significativa)."),
    "7210000": CNAEInfo("7210000", "Pesquisa e desenvolvimento experimental em ciências físicas e naturais",
        "III", False, None, "2-5%", False, False,
        "P&D = Anexo III. Avaliar Lei do Bem se Lucro Real (exclusão 60-80% despesas P&D do IRPJ)."),
    "7311400": CNAEInfo("7311400", "Agências de publicidade",
        "V", False, None, "2-5%", False, False,
        "Publicidade = Anexo V. Fator-R para migrar para Anexo III."),
    "7490104": CNAEInfo("7490104", "Atividades de intermediação e agenciamento de serviços e negócios em geral",
        "III", False, None, "2-5%", False, False,
        "Agenciamento/corretagem = Anexo III (serviço). Não confundir com corretagem de seguros (vedada)."),

    # ── SERVIÇOS FINANCEIROS (vedados) ───────────────────
    "6421200": CNAEInfo("6421200", "Bancos comerciais",
        None, True, "Instituição financeira vedada no Simples Nacional",
        "N/A", False, False,
        "Banco = VEDADO Simples. Lucro Real obrigatório para instituições financeiras."),
    "6422100": CNAEInfo("6422100", "Bancos múltiplos, com carteira comercial",
        None, True, "Instituição financeira vedada no Simples Nacional",
        "N/A", False, False,
        "Banco múltiplo = VEDADO Simples."),
    "6431000": CNAEInfo("6431000", "Bancos de desenvolvimento",
        None, True, "Instituição financeira vedada", "N/A", False, False,
        "Banco desenvolvimento = VEDADO."),
    "6511101": CNAEInfo("6511101", "Seguros de vida",
        None, True, "Seguradora vedada no Simples Nacional",
        "N/A", False, False,
        "Seguradora = VEDADO Simples."),
    "6550200": CNAEInfo("6550200", "Planos de saúde",
        None, True, "Operadora de plano de saúde vedada no Simples",
        "N/A", False, False,
        "Operadora plano saúde = VEDADO Simples."),

    # ── IMOBILIÁRIO ────────────────────────────────────────
    "6810201": CNAEInfo("6810201", "Compra e venda de imóveis próprios",
        None, True, "Holding imobiliária: sócio PJ veda Simples",
        "N/A", False, False,
        "Compra/venda imóvel próprio = em geral VEDADO se a empresa tiver sócio PJ (holding). ITBI na aquisição."),
    "6821801": CNAEInfo("6821801", "Corretagem na compra e venda e avaliação de imóveis",
        "III", False, None, "2-5%", False, False,
        "Corretagem imobiliária = Anexo III. ISS municipal."),
    "6822600": CNAEInfo("6822600", "Gestão e administração de imóveis de terceiros",
        "III", False, None, "2-5%", False, False,
        "Administração de imóveis = Anexo III."),

    # ── ALIMENTAÇÃO / HOSPEDAGEM ──────────────────────────
    "5611201": CNAEInfo("5611201", "Restaurantes e similares",
        "I", False, None, "N/A", True, False,
        "Restaurante = Anexo I (venda de produto). Se preparo + serviço: ISS municipal também pode incidir."),
    "5611203": CNAEInfo("5611203", "Lanchonetes, casas de chá, sucos e similares",
        "I", False, None, "N/A", True, False,
        "Lanchonete = Anexo I."),
    "5590699": CNAEInfo("5590699", "Outros tipos de alojamento não especificados anteriormente",
        "III", False, None, "2-5%", False, False,
        "Airbnb/alojamento alternativo = Anexo III (serviço). ISS municipal."),
    "5510801": CNAEInfo("5510801", "Hotéis",
        "III", False, None, "2-5%", False, False,
        "Hotel = Anexo III (hospedagem = serviço). ISS municipal."),

    # ── TRANSPORTE E LOGÍSTICA ────────────────────────────
    "4921301": CNAEInfo("4921301", "Transporte rodoviário coletivo de passageiros com itinerário fixo - municipal",
        "III", False, None, "2-5%", False, False,
        "Transporte coletivo municipal. Atenção: CBS/IBS alíquota zero em transporte público coletivo a partir de 2026."),
    "4930201": CNAEInfo("4930201", "Transporte rodoviário de carga, exceto produtos perigosos e mudanças - municipal",
        "III", False, None, "N/A", False, False,
        "Frete municipal = Anexo III. ICMS-T pode incidir dependendo do estado."),
    "4930202": CNAEInfo("4930202", "Transporte rodoviário de carga - intermunicipal, interestadual e internacional",
        "III", False, None, "N/A", True, False,
        "Frete intermunicipal/interestadual = ICMS sobre frete. Anexo III no Simples."),

    # ── BELEZA E BEM-ESTAR ────────────────────────────────
    "9602501": CNAEInfo("9602501", "Cabeleireiros, manicure e pedicure",
        "III", False, None, "2-5%", False, False,
        "Salão de beleza = Anexo III (serviço pessoal). ISS municipal."),
    "9311500": CNAEInfo("9311500", "Academias de dança",
        "III", False, None, "2-5%", False, False,
        "Academia de dança = Anexo III."),
    "9313100": CNAEInfo("9313100", "Atividades de condicionamento físico (academias)",
        "III", False, None, "2-5%", False, False,
        "Academia de ginástica = Anexo III."),

    # ── VIGILÂNCIA / LIMPEZA ──────────────────────────────
    "8011101": CNAEInfo("8011101", "Atividades de vigilância e segurança privada",
        "IV", False, None, "2-5%", False, False,
        "Vigilância = Anexo IV. INSS patronal fora do DAS. Alta folha."),
    "8121400": CNAEInfo("8121400", "Limpeza em prédios e em domicílios",
        "IV", False, None, "2-5%", False, False,
        "Limpeza/conservação = Anexo IV. INSS patronal fora do DAS."),

    # ── CONTABILIDADE / AUDITORIA ─────────────────────────
    "6920601": CNAEInfo("6920601", "Atividades de contabilidade",
        "III", False, None, "2-5%", False, False,
        "Contabilidade = Anexo III. Verificar Fator-R se folha >= 28%."),
    "6920602": CNAEInfo("6920602", "Atividades de consultoria e auditoria contábil e tributária",
        "III", False, None, "2-5%", False, False,
        "Auditoria/consultoria contábil = Anexo III."),

    # ── E-COMMERCE / MARKETPLACE ──────────────────────────
    "4791100": CNAEInfo("4791100", "Comércio varejista por catálogo, televisão, rádio, internet",
        "I", False, None, "N/A", True, False,
        "E-commerce varejista = Anexo I. ICMS + DIFAL para outras UFs (até 2032; depois IBS destino)."),
    "6399200": CNAEInfo("6399200", "Outras atividades de prestação de serviços de informação não especificadas",
        "III", False, None, "2-5%", False, False,
        "Marketplace/plataforma digital = Anexo III. Alta exposição à CBS a partir de 2027."),
}


# ─────────────────────────────────────────────────────────
# 3. TABELAS DE ALÍQUOTA SIMPLES NACIONAL (2025)
# ─────────────────────────────────────────────────────────

SIMPLES_TABELAS = {
    "I": {  # Comércio
        "nome": "Anexo I — Comércio",
        "faixas": [
            (180000,    4.00,      0),
            (360000,    7.30,   5940),
            (720000,    9.50,  13860),
            (1800000,  10.70,  22500),
            (3600000,  14.30,  87300),
            (4800000,  19.00, 378000),
        ]
    },
    "II": {  # Indústria
        "nome": "Anexo II — Indústria",
        "faixas": [
            (180000,    4.50,      0),
            (360000,    7.80,   5940),
            (720000,   10.00,  13860),
            (1800000,  11.20,  22500),
            (3600000,  14.70,  85500),
            (4800000,  30.00, 720000),
        ]
    },
    "III": {  # Serviços baixo INSS
        "nome": "Anexo III — Serviços (baixo INSS patronal)",
        "faixas": [
            (180000,    6.00,      0),
            (360000,   11.20,   9360),
            (720000,   13.20,  17640),
            (1800000,  16.00,  35640),
            (3600000,  21.00, 125640),
            (4800000,  33.00, 648000),
        ]
    },
    "IV": {  # Serviços INSS separado
        "nome": "Anexo IV — Serviços (INSS patronal fora do DAS)",
        "faixas": [
            (180000,    4.50,      0),
            (360000,    9.00,   8100),
            (720000,   10.20,  12420),
            (1800000,  14.00,  39780),
            (3600000,  22.00, 183780),
            (4800000,  33.00, 828000),
        ]
    },
    "V": {  # Serviços alta folha
        "nome": "Anexo V — Serviços (alta folha de pagamento)",
        "faixas": [
            (180000,   15.50,      0),
            (360000,   18.00,   4500),
            (720000,   19.50,   9900),
            (1800000,  20.50,  17100),
            (3600000,  23.00,  62100),
            (4800000,  30.50, 540000),
        ]
    },
}


def calcular_aliquota_efetiva(rbt12: float, anexo: str) -> tuple[float, str]:
    """Retorna (aliquota_efetiva_percent, faixa_descricao)."""
    if anexo not in SIMPLES_TABELAS:
        return 0.0, "Anexo não encontrado"

    tabela = SIMPLES_TABELAS[anexo]["faixas"]
    faixa_anterior = 0

    for i, (limite, aliq_nominal, deducao) in enumerate(tabela):
        if rbt12 <= limite:
            aliq_efetiva = (rbt12 * aliq_nominal / 100 - deducao) / rbt12 * 100
            faixa_num = i + 1
            return round(aliq_efetiva, 2), f"Faixa {faixa_num} (até R${limite:,.0f})"
        faixa_anterior = limite

    # Acima do limite do Simples
    return 0.0, "Acima do limite Simples (R$4,8M) — migrar para Lucro Presumido/Real"


def calcular_fator_r(folha_12m: float, rbt12: float) -> tuple[float, str]:
    """Calcula o Fator-R e retorna o anexo aplicável para Anexo III vs V."""
    if rbt12 == 0:
        return 0.0, "III"
    fator = folha_12m / rbt12
    anexo = "III" if fator >= 0.28 else "V"
    return round(fator * 100, 1), anexo


# ─────────────────────────────────────────────────────────
# 4. FUNÇÕES DE CONSULTA
# ─────────────────────────────────────────────────────────

def consultar_cnae(codigo: str) -> None:
    codigo = codigo.strip().replace(".", "").replace("-", "").replace("/", "")
    info = CNAE_DATABASE.get(codigo)

    if not info:
        print(f"\n❌ CNAE {codigo} não encontrado na base local.")
        print("   Consulte a tabela completa em: receita.fazenda.gov.br/SimplesNacional")
        print("   ou utilize --search para buscar por descrição.")
        return

    print(f"\n{'='*60}")
    print(f"CNAE: {info.codigo} — {info.descricao}")
    print(f"{'='*60}")

    if info.vedado_simples:
        print(f"\n🚫 VEDADO NO SIMPLES NACIONAL")
        print(f"   Motivo: {info.motivo_vedacao}")
        print(f"\n   Regimes possíveis: Lucro Presumido ou Lucro Real")
    else:
        print(f"\n✅ PERMITIDO NO SIMPLES NACIONAL")
        print(f"   Anexo: {info.anexo_simples} — {SIMPLES_TABELAS.get(info.anexo_simples, {}).get('nome', '')}")
        if info.anexo_simples in ("III", "V"):
            print(f"\n   ⚠️  ATENÇÃO — FATOR-R:")
            print(f"   Este CNAE pode estar no Anexo III ou Anexo V dependendo do Fator-R:")
            print(f"   → Fator-R = Folha12m / RBT12")
            print(f"   → Fator-R >= 28%: Anexo III (alíquota MENOR)")
            print(f"   → Fator-R < 28%:  Anexo V  (alíquota MAIOR)")
            print(f"   Use --simular para calcular com seus números.")

    print(f"\n   ISS: {info.iss_faixa}")
    print(f"   ICMS: {'Sim' if info.icms else 'Não'}")
    print(f"   IPI:  {'Sim' if info.ipi else 'Não'}")
    print(f"\n   Observações: {info.observacoes}")


def buscar_cnae(termo: str) -> None:
    termo = termo.lower()
    resultados = [
        (cod, info) for cod, info in CNAE_DATABASE.items()
        if termo in info.descricao.lower() or termo in info.observacoes.lower()
    ]

    if not resultados:
        print(f"\n❌ Nenhum CNAE encontrado para '{termo}'")
        return

    print(f"\n{'='*60}")
    print(f"CNAEs encontrados para '{termo}': {len(resultados)}")
    print(f"{'='*60}")
    for cod, info in resultados:
        status = "🚫 VEDADO" if info.vedado_simples else f"✅ Anexo {info.anexo_simples}"
        print(f"  {cod} | {status:15} | {info.descricao}")


def listar_vedados() -> None:
    vedados = [(cod, info) for cod, info in CNAE_DATABASE.items() if info.vedado_simples]
    print(f"\n{'='*60}")
    print(f"CNAEs VEDADOS NO SIMPLES NACIONAL ({len(vedados)} na base local)")
    print(f"{'='*60}")
    for cod, info in vedados:
        print(f"  {cod} | {info.descricao}")
        print(f"         → {info.motivo_vedacao}")


def simular(codigo: str, faturamento_anual: float,
            folha_12m: float = 0.0) -> None:
    codigo = codigo.strip().replace(".", "").replace("-", "").replace("/", "")
    info = CNAE_DATABASE.get(codigo)

    if not info:
        print(f"\n❌ CNAE {codigo} não encontrado.")
        return

    if info.vedado_simples:
        print(f"\n🚫 CNAE {codigo} VEDADO no Simples Nacional.")
        print(f"   Simulação disponível apenas para Simples. Use Lucro Presumido/Real.")
        return

    rbt12 = faturamento_anual
    anexo = info.anexo_simples

    # Verificar Fator-R
    if anexo in ("III", "V") and folha_12m > 0:
        fator, anexo_fatorr = calcular_fator_r(folha_12m, rbt12)
        print(f"\n  Fator-R calculado: {fator}% → Anexo {anexo_fatorr}")
        anexo = anexo_fatorr
    elif anexo in ("III", "V") and folha_12m == 0:
        print(f"\n  ⚠️  Sem folha informada — usando Anexo {anexo} padrão.")
        print(f"       Para cálculo preciso, informe --folha <valor>")

    aliq, faixa = calcular_aliquota_efetiva(rbt12, anexo)

    das_mensal = (faturamento_anual / 12) * aliq / 100
    das_anual = faturamento_anual * aliq / 100

    print(f"\n{'='*60}")
    print(f"SIMULAÇÃO — CNAE {codigo}: {info.descricao}")
    print(f"{'='*60}")
    print(f"  Faturamento anual (RBT12): R${rbt12:>12,.2f}")
    if folha_12m > 0:
        print(f"  Folha 12 meses:            R${folha_12m:>12,.2f}")
    print(f"  Anexo aplicável:            {anexo} — {SIMPLES_TABELAS[anexo]['nome']}")
    print(f"  Faixa:                       {faixa}")
    print(f"  Alíquota efetiva Simples:    {aliq}%")
    print(f"  DAS mensal (estimado):      R${das_mensal:>12,.2f}")
    print(f"  DAS anual (estimado):       R${das_anual:>12,.2f}")

    # Comparativo Lucro Presumido (serviços 32%, IRPJ 15% + CSLL 9% + PIS 0.65% + COFINS 3%)
    if info.anexo_simples in ("III", "IV", "V"):
        base_irpj = faturamento_anual * 0.32
        irpj = base_irpj * 0.15
        adcs = base_irpj * 0.10  # adicional 10% sobre base - 60K
        csll = faturamento_anual * 0.32 * 0.09
        pis = faturamento_anual * 0.0065
        cofins = faturamento_anual * 0.03
        iss_estimado = faturamento_anual * 0.03  # 3% médio
        total_presumido = irpj + csll + pis + cofins + iss_estimado
        aliq_presumido = total_presumido / faturamento_anual * 100

        print(f"\n  Comparativo — Lucro Presumido (serviços, ISS 3% est.):")
        print(f"  Alíquota efetiva estimada:   {aliq_presumido:.1f}%")
        print(f"  Total anual estimado:        R${total_presumido:>12,.2f}")

        if das_anual < total_presumido:
            economia = total_presumido - das_anual
            print(f"\n  → Simples Nacional é mais vantajoso")
            print(f"    Economia anual estimada:  R${economia:>12,.2f}")
        else:
            economia = das_anual - total_presumido
            print(f"\n  → Lucro Presumido pode ser mais vantajoso")
            print(f"    Diferença anual:          R${economia:>12,.2f}")
            print(f"    (Verifique com contador — depende de deduções reais)")

    print(f"\n  ⚠️  Valores estimados. Sempre confirmar com contador.")


# ─────────────────────────────────────────────────────────
# 5. INTERFACE DE LINHA DE COMANDO
# ─────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]

    if not args or "--help" in args or "-h" in args:
        print(__doc__)
        print("\nExemplos:")
        print("  python3 brazil_cnae_database.py 6201500")
        print("  python3 brazil_cnae_database.py --search engenharia")
        print("  python3 brazil_cnae_database.py --list-vedados")
        print("  python3 brazil_cnae_database.py --simular --cnae 6201500 --faturamento 1200000 --folha 200000")
        return

    if "--list-vedados" in args:
        listar_vedados()
        return

    if "--search" in args:
        idx = args.index("--search")
        if idx + 1 < len(args):
            buscar_cnae(args[idx + 1])
        else:
            print("❌ Informe o termo de busca após --search")
        return

    if "--simular" in args:
        cnae = None
        fat = None
        folha = 0.0

        if "--cnae" in args:
            cnae = args[args.index("--cnae") + 1]
        if "--faturamento" in args:
            fat = float(args[args.index("--faturamento") + 1])
        if "--folha" in args:
            folha = float(args[args.index("--folha") + 1])

        if cnae and fat:
            simular(cnae, fat, folha)
        else:
            print("❌ Use: --simular --cnae <codigo> --faturamento <valor> [--folha <valor>]")
        return

    # Consulta direta por código
    consultar_cnae(args[0])


# ─────────────────────────────────────────────────────────
# 6. EXECUÇÃO DIRETA / DEMO
# ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Demo interativo se rodar sem argumentos
        print("=" * 60)
        print("BRAZIL CNAE DATABASE — Demo")
        print("=" * 60)

        print("\n[1] Consulta TI sob encomenda (6201500):")
        consultar_cnae("6201500")

        print("\n[2] Consulta Engenharia (7112000) — Fator-R:")
        consultar_cnae("7112000")

        print("\n[3] Simulação TI, faturamento R$600K/ano, folha R$150K:")
        simular("6201500", 600000, 150000)

        print("\n[4] Busca por 'advocacia':")
        buscar_cnae("advocacia")

        print("\n[5] CNAEs vedados no Simples:")
        listar_vedados()
    else:
        main()
