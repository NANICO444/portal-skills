---
name: licitacoes
description: "Skill de licitacoes publicas - analise de editais, documentos, prazos, e propostas. Para mercado brasileiro."
user-invocable: true
allowed-tools: Read, WebFetch, Bash, Edit
---

# Licitacoes Publicas

## Quando Usar

- Analise de editais (PREGAO, CONCORRENCIA, TOMADA DE PRECOS, CONVITE, LEILAO, DIALOGO COMPETITIVO)
- Extracao de requisitos tecnicos de PDF/Word
- Checklist de habilitacao juridica, fiscal, tecnica
- Calculo de prazo de recurso / contrarrazoes
- Elaboracao de propostas tecnicas e comerciais
- Analise de impugnações e esclarecimentos

## Workflow Padrao

### Passo 1 - Identificar Modalidade
- PREGAO ELETRONICO: mais comum, lances online
- PREGAO PRESENCIAL: lances fisicos
- CONCORRENCIA: valores altos, fases
- TOMADA DE PRECOS: limite R$ 1.5M
- DIALOGO COMPETITIVO: novidade 2024+

### Passo 2 - Extrair Dados do Edital
- Objeto: o que sera contratado
- Valor estimado: preco de referencia
- Data de abertura: prazo
- Habilitacao: documentos exigidos
- Criterio de julgamento: menor preco, melhor tecnica, tecnica+preco

### Passo 3 - Checklist de Habilitacao

#### Juridica
- [ ] Ato constitutivo (contrato social, estatuto)
- [ ] CNPJ ativo
- [ ] RG/CPF dos socios
- [ ] Prova de representacao legal (procuracao se aplicavel)

#### Fiscal
- [ ] CND Federal
- [ ] CND Estadual
- [ ] CND Municipal
- [ ] FGTS (CRF)
- [ ] CNDT (Trabalhista)

#### Tecnica
- [ ] Atestado de capacidade tecnica
- [ ] CAT (Certidao de Acervo Tecnico)
- [ ] Registro profissional (CAU, CREA, CRM, etc)
- [ ] Visitas tecnicas (se exigida)

#### Economico-Financeira
- [ ] Balanco patrimonial
- [ ] Indices (Liquidez Geral, Solvencia, Endividamento)
- [ ] Certidao negativa de falencia

### Passo 4 - Analise de Riscos
- Prazo de execucao viavel?
- Equipe tecnica disponivel?
- Margem de lucro (minimo 10%)?
- Garantias exigidas compativeis?
- Cláusula de reequilibrio economico-financeiro?

### Passo 5 - Proposta
- Identificada: razao social, CNPJ
- Endereco completo
- Valores (unitario, total)
- Prazo de validade (min 60 dias)
- Prazo de execucao
- Garantia
- Declaracoes exigidas

## Glossario de Termos

- **SRP**: Sistema de Registro de Preco
- **ARP**: Ata de Registro de Preco
- **Ordenador de Despesas**: autoridade que assina o contrato
- **Pregoeiro**: quem conduz o pregao
- **Impugnacao**: questionamento do edital (5 dias uteis antes)
- **Esclarecimento**: duvida sobre o edital (3 dias uteis antes)
- **Recurso**: contestacao do resultado (3 dias uteis)
- **Contrarrazoes**: defesa contra recurso (3 dias uteis)
- **Sancao Administrativa**: penalidade (advertencia, multa, suspensao, declaracao de inidoneidade)

## Documentos Frequentes

- Termo de Referencia (TR) - anexos importantes
- Projeto Basico (obras)
- Minuta de Contrato
- Planilha de Custos (BDI max 30% para obras)
- Cronograma Fisico-Financeiro
- Especificacoes tecnicas

## Portais para Pesquisa

- **ComprasNet / Compras.gov**: federal
- **BEC/SP**: estado de Sao Paulo
- **Licitacoes-e**: Banco do Brasil
- **Portal da Transparencia**: sancoes e contratos
- **PNCP**: Portal Nacional de Contracoes Publicas (obrigatorio desde 2024)
- **TCU**: jurisdicionados
- **CGE**: controle interno estadual

## Frameworks Uteis

- `skill:web-fetch` - para buscar editais
- `skill:web-scrape` - para extrair de portais
- `skill:ocr` - para PDFs digitalizados
- `skill:code-review` - para revisar proposta tecnica

## Anti-Padroes

- Assinar proposta sem ler todo o edital
- Esquecer de calcular BDI corretamente
- Nao verificar prazo de validade
- Esquecer de declaracoes obrigatorias
- Subestimar prazo de execucao

## Output Esperado

```
ANALISE DE EDITAL - [NUMERO]

MODALIDADE: [pregao eletronico / etc]
ORGAO: [nome]
OBJETO: [descricao]
VALOR ESTIMADO: R$ X
DATA DE ABERTURA: DD/MM/YYYY

HABILITACAO NECESSARIA:
- Juridica: [lista]
- Fiscal: [lista]
- Tecnica: [lista]
- Economico-Financeira: [lista]

RISCOS IDENTIFICADOS:
1. [risco + mitigacao]
2. [risco + mitigacao]

DECISAO: PARTICIPAR / NAO PARTICIPAR

PROXIMOS PASSOS:
1. [acao]
2. [acao]
```
