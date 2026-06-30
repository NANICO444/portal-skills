# MODULO: CRIACAO DE SITES
# Ultra Prompt v6.2 — Combo Module Full-Stack Site Creation
# Versao: 1.1.0 | Atualizado: 2026-04-20

---

## 0. QUANDO CARREGAR

Carregar quando usuario pede para criar site, landing page, portfolio, e-commerce, blog, webapp, dashboard, ou qualquer projeto web completo.

NAO carregar para: editar site existente (apenas fix), criar API sem interface, design isolado.

---

## 0.5 INTEGRACAO COM CORE.MD

Este modulo opera DENTRO do modelo de orquestracao do core.md (Secao 6):
- Core.md controla alocacao de sub-agentes (5-15, padrao Opus 4.7)
- Monitor Agent (SKILL 03 do core) roda automaticamente — este modulo NAO spawna monitor
- Persistence Agent (SKILL 02 do core) gerencia WAL — este modulo NAO duplica persistencia
- Este modulo e um EXECUTOR DE DOMINIO: define O QUE fazer para sites, core.md define COMO orquestrar
- Limite de subagentes: definido por core.md (5-15). Se site requer mais componentes que subagentes disponiveis:
  1. Agrupar componentes relacionados no mesmo subagent (ex: Header + Footer)
  2. Executar componentes simples inline (<30 linhas)
  3. Priorizar Tier 1 (Header, Hero, Footer) para subagentes dedicados
  4. Tier 2/3 executar inline ou agrupar se necessario

---

## 0.6 TOKEN BUDGET

- Modulo em contexto: ~5K tokens
- Skill files (sob demanda via Read): ~1.5K cada, max 3 simultaneos = ~4.5K
- Debate gates (checkpoints): ~500 tokens cada (8 campos) × 6 gates = ~3K
- Subagent prompts (efemeros): ~800 cada
- Design contract + state: ~1K
- **Pico estimado:** ~15K tokens (Fase 3 com debates + skills + subagentes ativos)
- **Gestao:** Comprimir debates apos aprovacao para "DECISAO + mitigacoes" (~150 tokens). Descarregar skill files apos uso da fase. Se contexto > 150K: acionar protocolo de compactacao do core.md.

---

## 1. WORKFLOW PHASES

```
FASE 1: ORQUESTRAR (planejar)
    ↓ [DEBATE GATE]
FASE 2: DECOMPOR (dividir em componentes)
    ↓ [DEBATE GATE]
FASE 3: PARALELIZAR (subagentes constroem)
    ↓ [DEBATE GATE]
FASE 4: INTEGRAR (montar tudo)
    ↓ [DEBATE GATE]
FASE 5: AUDITAR (testar e corrigir)
    ↓ [DEBATE GATE]
FASE 6: DEPLOY (colocar online)
    ↓ [Git commit final]
FASE 7: ENTREGAR (confirmar ao usuario)
```

### FASE 1 — ORQUESTRAR

**Pre-flight:** Verificar que Git funciona (`git --version`). Se nao → avisar usuario.

1. Extrair do pedido: tipo de site, paginas, funcionalidades, estilo, publico
2. Read `/skills/site/frontend.md` → extrair stack da tabela "STACKS RECOMENDADAS" cruzando com tipo de site → declarar: "Stack escolhida: [X] porque [razao]"
3. Read `/skills/site/palette.md` → gerar paleta baseada no tom do site → declarar: "Paleta: primary=[HEX], accent=[HEX]"
4. Criar `.design-contract.yml` (ver Secao 4)
5. Git: `git init` + commit "feat: initial planning and design contract"

### FASE 2 — DECOMPOR

1. Mapear componentes: header, footer, hero, paginas, formularios, etc.
2. Classificar dependencias (quais podem ser paralelos)
3. Read `/skills/site/content.md` → gerar conteudo contextual (NAO Lorem Ipsum) → declarar: "Tom de conteudo: [X]"
4. Criar task list para subagentes com estimativa de complexidade

### FASE 3 — PARALELIZAR

**Pre-flight:** Verificar .design-contract.yml existe e esta commitado.

1. Para CADA subagente: preencher template (Secao 5) com dados extraidos dos skill files
2. Spawnar componentes independentes em PARALELO (max conforme core.md Section 6.3)
3. Componentes dependentes: aguardar predecessores
4. Git commit ao receber cada componente: "feat: add [component]"

### FASE 4 — INTEGRAR

1. Verificar Design Contract seguido (cores, espacamento consistentes)
2. Resolver conflitos de imports/dependencias
3. Montar routing/navigation
4. Build: rodar comando de build do framework
5. Corrigir erros de build
6. Git commit: "feat: integrate all components"

### FASE 5 — AUDITAR

**Pre-flight:** Verificar que site builda (`npm run build` ou equiv) ANTES de testar.

1. Read `/skills/site/testing.md` → executar protocolo completo
2. Se testing.md indisponivel: build + links + responsivo 320px/1280px + console errors
3. Read `/skills/site/performance.md` → aplicar otimizacoes
4. Corrigir issues encontrados, re-testar
5. Git commit: "fix: address audit findings"

**Gate:** Build DEVE passar sem erros criticos para avancar.

### FASE 6 — DEPLOY

**Pre-flight:** Verificar conexoes Maton ANTES de qualquer deploy attempt.

1. Read `/skills/site/deploy.md` → seguir protocolo completo
2. Verificar URL final acessivel (HTTP 200 + conteudo correto)
3. Git commit final: "chore: deploy to [platform]"

### FASE 7 — ENTREGAR

```
SITE ENTREGUE
URL: [link]
Repositorio: [link GitHub]
Stack: [framework + ferramentas]
Paginas: [lista]
Proximos passos: [1-2 sugestoes]
```

---

## 2. DEBATE PROTOCOL — GATES ESTRUTURAIS

> O agente NAO avanca para proxima fase sem produzir debate visivel que atenda os criterios.

### Formato (visivel no chat)

```
═══ DEBATE GATE: [Fase] ═══
DECIDINDO: [pergunta central]
A FAVOR: [2 argumentos pro opcao escolhida]
CONTRA: [2 argumentos/riscos]
RISCO 1: [descricao] → Mitigacao: [acao]
RISCO 2: [descricao] → Mitigacao: [acao]
ALTERNATIVA: [opcao descartada + motivo]
DECISAO: [escolha] | CONFIANCA: [ALTA/MEDIA/BAIXA]
═══ GATE APROVADO ═══
```

### Verificacao de Qualidade

Debate SO e valido se contem:
- Minimo 2 riscos COM mitigacao
- Minimo 1 alternativa real (nao strawman)
- Justificativa tecnica ou baseada em requisito do usuario

Se nao atende → refazer. NAO seguir em frente com debate incompleto.

### Quando Debater (por fase)

| Fase | Foco do Debate |
|------|---------------|
| 1→2 | Stack + arquitetura + framework |
| 2→3 | Divisao de trabalho + dependencias |
| 3→4 | Qualidade dos componentes recebidos |
| 4→5 | Integracao OK? Build passa? |
| 5→6 | Testes passaram? Pronto para deploy? |
| Erro | Diagnostico: causa + fix + alternativa |

---

## 3. SKILL FILE LOADING — PROTOCOLO

### Regra

ANTES de cada fase que requer conhecimento de dominio:
1. Executar Read no skill file correspondente
2. EXTRAIR dado especifico (ver tabela abaixo)
3. DECLARAR no chat o que extraiu (prova de leitura)
4. USAR o dado extraido na fase

### Mapa de Extracao

| Fase | Skill File | O que extrair | Declarar |
|------|-----------|---------------|----------|
| 1 | frontend.md | Tabela "STACKS RECOMENDADAS" → cruzar com tipo | "Stack: [X]" |
| 1 | palette.md | Tom + cores baseado no tipo de site | "Primary: [HEX], Accent: [HEX]" |
| 2 | content.md | Tom e formulas de conteudo | "Tom: [formal/casual/tech]" |
| 5 | testing.md | Categorias de teste aplicaveis | "Testando: [lista]" |
| 5 | performance.md | Otimizacoes aplicaveis ao stack | "Otimizando: [lista]" |
| 6 | deploy.md | Plataforma detectada via Maton | "Deploy em: [plataforma]" |
| Erro | recovery.md | Decision tree aplicavel | "Seguindo DT-[N]" |

### Fallback (se Read falhar)

1. Registrar: "ALERTA: [skill] nao encontrado. Modo basico."
2. Usar conhecimento interno do modelo (treinamento)
3. Marcar no debate que esta operando sem skill file

---

## 4. DESIGN CONTRACT

Todo projeto DEVE ter `.design-contract.yml` commitado ANTES de construir componentes.

```yaml
# .design-contract.yml
project:
  name: "[nome]"
  type: "[landing|ecommerce|blog|dashboard|portfolio|saas]"
  stack: "[next.js|astro|html-css|remix|sveltekit]"
colors:
  primary: "#HEXVAL"
  secondary: "#HEXVAL"
  accent: "#HEXVAL"
  background: "#HEXVAL"
  surface: "#HEXVAL"
  text: "#HEXVAL"
  text_muted: "#HEXVAL"
typography:
  heading_font: "Font Name"
  body_font: "Font Name"
  base_size: "16px"
  scale: "1.25"
spacing:
  unit: "4px"
  component_gap: "16px"
  section_padding: "64px"
  container_max: "1280px"
breakpoints:
  mobile: "320px"
  tablet: "768px"
  desktop: "1280px"
```

**Regra:** Qualquer componente que usa cor/fonte diferente do contrato = BUG a ser corrigido.

---

## 5. SUBAGENT PROMPT TEMPLATES

### Template: Componente Frontend

```
Voce esta construindo [COMPONENTE] para um site [STACK].

DESIGN CONTRACT:
- Cores: primary=[HEX], secondary=[HEX], accent=[HEX], bg=[HEX], text=[HEX]
- Tipografia: heading=[FONT], body=[FONT]
- Espacamento: gap=[N]px, section-padding=[N]px
- Breakpoints: 320px / 768px / 1280px

REQUISITOS:
- [Req funcional 1]
- [Req funcional 2]

RESTRICOES:
- Mobile-first, semantic HTML, acessibilidade basica (ARIA, alt text, keyboard)
- ZERO placeholders. Codigo production-ready completo.
- Salvar em: [caminho/arquivo]
```

### Template: Backend/API

```
Voce esta construindo [ENDPOINT] para [STACK].
- Validacao de input obrigatoria
- Error handling com mensagens claras
- NUNCA expor credenciais ou stack traces
- Salvar em: [caminho/arquivo]
```

### Template: Auditoria

```
Audite o site em [CAMINHO]. Verifique:
1. Build funciona?
2. Links internos validos?
3. Design Contract seguido? (cores, fontes)
4. Responsivo (320/768/1280)?
5. Acessibilidade (alt, semantic, ARIA)?

Reporte: severidade + arquivo:linha + fix sugerido.
Se aprovado: "APROVADO — pronto para deploy"
```

---

## 6. GITHUB BACKUP

| Momento | Commit Message |
|---------|---------------|
| Apos FASE 1 | `feat: initial planning and design contract` |
| Apos cada componente | `feat: add [component-name]` |
| Apos integracao | `feat: integrate all components` |
| Apos correcoes | `fix: [descricao]` |
| Apos deploy | `chore: deploy to [platform]` |

Regras:
- Repo privado por padrao (criar com github_helpers.py ou `gh repo create --private`)
- Commits atomicos (1 mudanca logica = 1 commit)
- ANTES de operacao arriscada → commit preventivo
- Se Git indisponivel → ZIP + avisar usuario

---

## 7. ERROR RECOVERY

Quando qualquer fase FALHA:

1. Read `/skills/site/recovery.md` → identificar Decision Tree aplicavel → declarar "Seguindo DT-[N]"
2. Aplicar Plan B do DT
3. Se Plan B falhar → Aplicar Plan C
4. Se Plan C falhar → PARAR + commitar estado + reportar ao usuario com:
   - O que foi feito
   - O que falhou e por que
   - Sugestao para resolver manualmente

**Regras:**
- 1 falha → Plan B
- 2 falhas mesmo problema → Plan C
- 3 falhas mesmo problema → PARAR e reportar
- NUNCA loop infinito de retry
- NUNCA apagar trabalho feito
- NUNCA fingir que resolveu

---

## 8. CONFLITO DE REGRAS

Prioridade (maior para menor):
1. Seguranca (nunca expor credenciais, repo privado)
2. Pedido explicito do usuario
3. Design Contract
4. Skill files
5. Conhecimento interno do modelo

Se usuario contradiz Design Contract → perguntar: "O contrato diz X, voce quer Y. Atualizo o contrato?"

---

*Modulo Site Creation v1.1.0 — Ultra Prompt v6.2*
*7 Fases | 6 Debate Gates | 7 Skill Files | Integrado com core.md*
