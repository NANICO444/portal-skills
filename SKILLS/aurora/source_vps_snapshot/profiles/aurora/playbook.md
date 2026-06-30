# Aurora — Playbook Operacional

Detalhes operacionais do workflow Aurora. Carregado sob demanda quando ela precisa de instrução técnica concreta.

**Última atualização**: 2026-05-21
**Origem**: composição de Drive Ultra Prompt v6.2 + GPT research design + decisões internas

---

## §1. Workflow 8 fases (com FASE -1)

### FASE -1 — Triage de Personas ⭐ (NOVA)

**Função**: Aurora planeja ordem de ativação de personas ANTES de qualquer fase. Evita carregar 10 personas de uma vez (inflaria contexto).

**Processo**:
1. Analisa pedido com modulações default (UI Designer + UX Architect)
2. Consulta templates registrados em `personas/README.md`:
   - Landing SaaS → Brand + Content + Visual + SEO + reviewers
   - Dashboard interno → defaults + Content (microcopy) + reviewers
   - Audit standalone → direto FASE 5 com reviewers
   - etc
3. **Tarefa CONHECIDA** (template) → triagem automática
4. **Tarefa NOVA/AMBÍGUA** → propõe ordem ao requester (Apollo/Jarvis/usuário), espera confirmação
5. Define ordem de ativação por fase
6. **Sugere triggers** úteis pro Miguel (mesmo que ele não use)
7. Procede pra FASE 0

**Output**: plano interno de personas + lista de triggers sugeridos.

### FASE 0 — Brief

**Função**: capturar contexto antes de criar qualquer pixel.

**Captura obrigatória**:
- Público (quem vai usar/ver)
- Objetivo (o que essa peça precisa fazer)
- Canal (web/email/social/print/app)
- Tom (corporativo, casual, moderno, brutalist, etc)
- Restrições (cores de marca obrigatórias, fontes proibidas, dark mode, mobile-only, etc)
- CTA (qual ação desejada)

**Bloqueia**: criação sem 3+ desses itens preenchidos.

**Modulação ativa**:
- Brand Guardian (se marca existente) — carrega `personas/brand-guardian.md`
- Content Creator (se já tem copy claro) — carrega `personas/content-creator.md`

### FASE 1 — Mood (3 direções obrigatórias)

**Função**: apresentar 3 caminhos visuais concretos antes de investir em artefato final.

**Cada direção tem**:
- Nome (ex: "Editorial Calmo", "Brutalist Bold", "Soft Minimal")
- Paleta inicial (5-6 cores OKLCH com papéis)
- Tipografia (par de fontes + razão)
- Referência (1-2 exemplos reais)
- Layout provável (1 frase descrevendo composição)
- Quando usar / quando não usar
- Risco de parecer genérico

**Decisão Miguel/requester**:
- Escolhe 1 direção (avança pra FASE 2)
- Mistura 2 direções (avança com proposta combinada)
- Pede mais (volta com 3 novas — máximo 1 rodada extra)
- Sem escolha → não investe em artefato (escala pro Apollo)

**[DEBATE GATE]** — Pro arquiteto propõe → Qwen revisor revisa antes de devolver.

### FASE 2 — Tokens (Workflow Master)

**Função**: gerar contrato visual completo.

**7 etapas** (origem Ultra Prompt v6.2):
1. Cor primária a partir do brief/marca
2. Escala 50-900 via OKLCH (variar lightness, manter hue)
3. Cor secundária por harmonia (complementar/análoga/triádica)
4. Cor de acento para CTAs
5. Neutrals tingidos (cinzas) — NUNCA preto/branco puros
6. Semânticas: success, warning, error, info
7. Validar contraste WCAG AA (4.5:1 texto, 3:1 UI) em todas combinações
8. Variante dark mode (inverter lightness, saturação -10%)

**Tipografia**:
- Font display (headings) — preferir Google Fonts via API
- Font body — harmonizar com display
- Escala 1.25 (minor third) ou 1.333 (perfect fourth)
- Pesos: 400, 500, 600, 700
- Line-height: 1.5 body, 1.2 headings, 1.75 texto longo
- Letter-spacing: normal body, -0.02em headings grandes
- Mínimo 16px body em mobile (evita zoom iOS)

**Espaçamento**:
- Unidade base 4px
- Escala: xs(4), sm(8), md(16), lg(24), xl(32), 2xl(48), 3xl(64)
- Grid: 12 colunas, gutter 16px mobile / 24px desktop
- Container max-width: 1280px

**Output**: JSON tokens completo (formato §10).

### FASE 3 — Componentes + Conteúdo (paralelo)

**Componentes** (Tier 1/2/3 — origem Drive `skills/site/component-library.md`):
- Tier 1: header/nav, hero, footer, button, card, contact form, FAQ/accordion
- Tier 2: gallery, testimonials, pricing table, CTA section
- Tier 3: blog grid, comparison table, timeline, stats

**Conteúdo** (origem Drive `skills/site/content.md`):
- Copy por seção (hero, benefícios, social proof, sobre, footer)
- Frameworks: PAS, AIDA, Before/After/Bridge, 4 U's
- Microcopy obrigatório (estados vazios, erros, loading, sucesso)

**Stack** (origem Drive `skills/site/frontend.md`):
- Decisão: HTML/CSS/JS vanilla vs Astro vs Next.js vs SvelteKit
- Critério: complexidade do projeto + necessidade de interatividade

**[DEBATE GATE]** — Impeccable `shape` command antes de build.

### FASE 4 — Build (frontend completo)

**Função**: codar artefato real.

**Stack já definida na FASE 3**:
- HTML/CSS/JS vanilla pra protótipo ou landing simples
- Next.js pra app fullstack
- Vue/Svelte se projeto exigir

**Padrões**:
- Mobile-first (320px base, scale up)
- Semantic HTML antes de div+ARIA
- CSS custom properties (variáveis = tokens da FASE 2)
- Component-based (mesmo HTML/CSS, reutilizável)
- Lazy loading imagens
- Fonts `display: swap`

**State management**:
- Local: `useState`, `useReducer`
- Compartilhado simples: Context API
- Compartilhado complexo: Zustand
- Server state: TanStack Query (React Query)

**Consumo de API**:
- Ler spec em `/srv/workspace/_shared/contracts/<projeto>/api/openapi-vN.yaml`
- Implementar consumo (fetch/axios)
- Validar contrato em runtime quando possível (Zod)

**Micro-debates a cada componente** — Impeccable `critique` no que acabou de fazer.

### FASE 5 — Gate Pré-Entrega ⭐ OBRIGATÓRIO

**Função**: validação multi-perspectiva antes de qualquer entrega.

**Sequência**:
1. **Impeccable audit + polish** — Aurora roda comandos:
   - `craft` (revisa estrutura geral)
   - `critique` (encontra anti-padrões)
   - `audit` (relatório completo)
   - `polish` (correções automáticas onde possível)

2. **3 Reviewers auto-ativados** (carregam personas individuais):
   - **Accessibility Auditor** (`personas/accessibility-auditor.md`)
   - **Performance Benchmarker** (`personas/performance-benchmarker.md`)
   - **Reality Checker** (`personas/reality-checker.md`)

3. **Browser-testing protocol** (origem Drive `skills/site/testing.md`):
   - Build test (passa sem erro?)
   - Testes funcionais (clicks, forms, navegação)
   - Testes responsivos (320px, 640px, 768px, 1024px, 1280px, 1536px)
   - WCAG AA (keyboard, contraste, ARIA)
   - SEO básico (h1, meta, OG)
   - Performance básica (LCP/INP/CLS)

**Se QUALQUER reviewer reprovar**:
- Volta pra FASE 4 com correções específicas
- Max 2 rodadas — depois: escala pro Apollo
- Aurora documenta gaps aceitos (se houver) em DECISIONS.md

### FASE 6 — Delivery

**Função**: entregar oficialmente.

**Sequência**:
1. **`kanban_complete`** com `summary` + `metadata` estruturado
2. **Pasta `entregas/<task-id>/`** completa:
   ```
   entregas/<task-id>/
   ├── README.md          # índice
   ├── CHANGELOG.md       # mudanças vs versões anteriores
   ├── DECISIONS.md       # tradeoffs assumidos
   ├── TESTING.md         # como testar + casos cobertos
   ├── DESIGN.md          # tokens
   ├── handoff/           # specs pra Hefesto se houver integração
   └── artifacts/         # HTML/CSS/JS, mockups
   ```
3. **Deploy STAGING** (via Maton API Gateway):
   - Repo GitHub PRIVADO (sempre)
   - Vercel/Netlify preview URL (NÃO produção)
4. **Drive entrega final** (se Miguel pediu):
   - `Aurora/<projeto>/entregas-finais/<data>_<nome>.<ext>`
5. **Notion atualizado** (se design system completo):
   - Página em "Design Systems" do workspace Miguel
6. **`_INDEX.md` do projeto atualizado** com entrega + links

**Aurora entrega pro Miguel**:
- Link staging (Vercel/Netlify)
- Link repo GitHub (privado)
- Link folder Drive (se aplicável)
- Link Notion (se aplicável)
- Resumo do que foi feito (1 parágrafo)

---

## §2. Workflow Master de Tokens (Detalhe FASE 2)

Origem: `modules_design.md` do Ultra Prompt v6.2.

### Template JSON tokens completo

```json
{
  "$schema": "https://opensource.adobe.com/spectrum-tokens/schemas/tokens.json",
  "colors": {
    "primary": {
      "50":  "oklch(0.98 0.02 142)",
      "100": "oklch(0.95 0.05 142)",
      "200": "oklch(0.88 0.10 142)",
      "300": "oklch(0.78 0.15 142)",
      "400": "oklch(0.65 0.18 142)",
      "500": "oklch(0.52 0.20 142)",
      "600": "oklch(0.42 0.18 142)",
      "700": "oklch(0.34 0.15 142)",
      "800": "oklch(0.26 0.12 142)",
      "900": "oklch(0.18 0.08 142)"
    },
    "neutral": {
      "50":  "oklch(0.98 0.01 240)",
      "500": "oklch(0.55 0.02 240)",
      "900": "oklch(0.15 0.02 240)"
    },
    "semantic": {
      "success": "oklch(0.65 0.18 145)",
      "warning": "oklch(0.75 0.18 75)",
      "error":   "oklch(0.62 0.22 25)",
      "info":    "oklch(0.62 0.18 240)"
    }
  },
  "typography": {
    "fontFamily": {
      "display": "'Crimson Pro', Georgia, serif",
      "body":    "'Inter Variable', system-ui, sans-serif",
      "mono":    "'JetBrains Mono', Menlo, monospace"
    },
    "fontSize": {
      "xs":   "0.75rem",
      "sm":   "0.875rem",
      "base": "1rem",
      "lg":   "1.125rem",
      "xl":   "1.25rem",
      "2xl":  "1.5rem",
      "3xl":  "1.875rem",
      "4xl":  "2.25rem"
    },
    "lineHeight": {
      "tight":   1.2,
      "normal":  1.5,
      "relaxed": 1.75
    },
    "letterSpacing": {
      "tight":  "-0.02em",
      "normal": "0",
      "wide":   "0.05em"
    }
  },
  "spacing": {
    "0":  "0",
    "1":  "0.25rem",
    "2":  "0.5rem",
    "3":  "0.75rem",
    "4":  "1rem",
    "6":  "1.5rem",
    "8":  "2rem",
    "12": "3rem",
    "16": "4rem",
    "24": "6rem"
  },
  "borderRadius": {
    "none": "0",
    "sm":   "0.25rem",
    "md":   "0.5rem",
    "lg":   "1rem",
    "xl":   "1.5rem",
    "full": "9999px"
  },
  "shadow": {
    "sm": "0 1px 2px rgba(0,0,0,0.05)",
    "md": "0 4px 6px rgba(0,0,0,0.1)",
    "lg": "0 10px 15px rgba(0,0,0,0.1)",
    "xl": "0 20px 25px rgba(0,0,0,0.15)"
  },
  "breakpoints": {
    "sm":  "640px",
    "md":  "768px",
    "lg":  "1024px",
    "xl":  "1280px",
    "2xl": "1536px"
  }
}
```

### Validação obrigatória

- [ ] Contraste WCAG AA em todas combinações texto/fundo
- [ ] Type scale legível em mobile (>= 16px body)
- [ ] Spacing cobre todos os casos sem lacunas
- [ ] Dark mode definido e testado
- [ ] Exportado no formato correto (CSS vars, JSON, Tailwind config)
- [ ] Zero valores "mágicos" fora do sistema

---

## §3. Responsive Mobile-First Workflow

Origem: `modules_design.md` do Ultra Prompt v6.2.

**Princípio**: começar em 320px, adicionar complexidade conforme espaço aumenta. **NUNCA desktop-first.**

### 6 Breakpoints + comportamento

| Breakpoint | Range | Comportamento |
|---|---|---|
| **mobile** | 320-639px | Coluna única, hamburger/bottom nav, touch 44x44px min, font 16px base, padding 16px |
| **sm** | 640-767px | Grid 2 colunas, tab bar horizontal, sidebar oculta, padding 24px |
| **md** | 768-1023px | Grid 2-3 colunas, sidebar mini/overlay, campos lado a lado, padding 32px |
| **lg** | 1024-1279px | Sidebar + conteúdo, grid 3-4 colunas, hover via `@media (hover: hover)`, nav completa |
| **xl** | 1280-1535px | Container max-width 1280px, centralizado, 4+ colunas |
| **2xl** | 1536px+ | Dashboards multi-painel, max-width 1536px |

### Testes obrigatórios

- [ ] 320px (iPhone SE) — legível e acessível?
- [ ] 375px (iPhone) — sem overflow horizontal?
- [ ] 768px (iPad portrait) — grid adapta?
- [ ] 1024px (laptop) — sidebar aparece?
- [ ] 1440px (desktop) — container não estica?
- [ ] Portrait + landscape em todos

### Touch vs Mouse

- **Touch**: áreas grandes, sem hover-dependent UI
- **Mouse**: hover, tooltips
- **Híbrido**: `@media (hover: hover)`
- **Teclado**: tab order, focus visible

---

## §4. WCAG 2.1 AA Checklist

Origem: `modules_design.md` + Drive `skills/site/accessibility-audit.md`.

### Top 10 Rápido (TODA entrega)

1. Contraste >= 4.5:1 texto principal
2. Alt text em imagens significativas
3. Navegação por teclado completa
4. Focus visível em TUDO
5. Labels em inputs (via `for`/`id`)
6. Skip navigation como primeiro focável
7. HTML semântico (h1-h6, landmarks)
8. `prefers-reduced-motion` implementado
9. Touch targets >= 44x44px
10. HTML válido (sem tags abertas, IDs duplicados)

### Completo (4 categorias)

**Percepção**: contraste, alt text, cor não-única-indicador, zoom 200%, espaçamento texto

**Operabilidade**: teclado, tab order, focus visível, skip nav, sem trap, touch target, sem flash >3x/s, reduced motion

**Compreensão**: `lang="pt-BR"`, labels, erros claros, formato esperado visível, navegação consistente, confirmação destrutiva

**Robustez**: HTML válido, ARIA correto (HTML semântico > ARIA roles), nome acessível, `aria-live` em mudanças dinâmicas

---

## §5. Design Systems Workflow

Origem: `modules_design.md`.

### 5 Fases

**Fase 1 — Auditoria Visual**
- Coletar telas/páginas existentes
- Inventariar cores, fontes, espaçamentos, radius, shadows únicos
- Mapear inconsistências (ex: 14 cinzas diferentes)
- Priorizar: cores > tipografia > espaçamento > componentes

**Fase 2 — Tokens** (seguir §2 Workflow Master)

**Fase 3 — Componentes** (ordem de criação)
1. Tipografia (h1-h6, body, caption, link)
2. Botões (primary, secondary, ghost, danger + TODOS estados)
3. Inputs (text, textarea, select, checkbox, radio, toggle + estados)
4. Cards (default, elevated, outlined, interactive)
5. Navigation (header, sidebar, breadcrumbs, tabs, pagination)
6. Feedback (alerts, toasts, badges, progress, skeletons, empty states)
7. Layout (container, grid, stack, divider)
8. Overlays (modal, drawer, popover, tooltip, dropdown)

**Fase 4 — Documentação por Componente**
Pra CADA componente: nome | variantes | props | TODOS estados | anatomia | quando usar/NÃO usar | código mínimo | ARIA + keyboard behavior

**Fase 5 — Manutenção**
- Mudança de token = revisar todos componentes que usam
- Novos componentes = SOMENTE tokens existentes
- Depreciação: 2 versões antes de remover
- Changelog com data + motivo + impacto
- Semver: breaking=major, novo=minor, fix=patch

---

## §6. UI Review Checklist

Origem: `modules_design.md`.

### Visual
- [ ] Hierarquia clara (título > subtítulo > body > caption)
- [ ] Alinhamento e espaçamento consistentes
- [ ] Cores e tipografia seguem tokens
- [ ] White space suficiente

### Técnico
- [ ] HTML válido e semântico
- [ ] CSS sem `!important` desnecessário
- [ ] Performance (imagens otimizadas, fonts display:swap)
- [ ] Responsivo em 320px, 768px, 1280px min
- [ ] Zero valores hardcoded fora do sistema

### Acessibilidade
- [ ] Top 10 WCAG executado (§4)
- [ ] Navegação por teclado testada
- [ ] Contraste verificado em produção (não só IDE)

### Conteúdo
- [ ] Texto real (não Lorem Ipsum) nas áreas principais
- [ ] Textos longos/curtos testados (overflow, truncation)
- [ ] Empty states com mensagem + CTA
- [ ] Erros claros e acionáveis

**Aprovação**: zero issues críticos | max 2 issues menores documentados.

---

## §7. Design Handoff Workflow (pra Hefesto)

Origem: `modules_design.md` + Compliance Aurora-Hefesto (§9).

### Assets
- Ícones: SVG (preferido) ou PNG @2x
- Fotos: WebP (fallback JPG)
- Logos: SVG + PNG em 3 tamanhos
- Nomes descritivos: `icon-arrow-right.svg`, `hero-bg.webp`

### Specs por tela
- Espaçamentos exatos (px e rem)
- Cores (referência ao token, não hex direto)
- Tipografia (font, size, weight, line-height, color)
- Comportamento responsivo por breakpoint
- Estados interativos (hover, focus, active, disabled)
- Animações (propriedade, duration, easing)

### Checklist Handoff
- [ ] Tokens exportados (JSON + CSS vars)
- [ ] Assets exportados e nomeados
- [ ] Specs documentadas por tela
- [ ] Breakpoints + responsivo descrito
- [ ] Estados interativos documentados
- [ ] Edge cases cobertos (texto longo, lista vazia, erro, loading)
- [ ] Notas de acessibilidade (tab order, ARIA, focus)

### Formato
Pasta organizada: `entregas/<task-id>/handoff/`
- `/tokens` — JSON + CSS vars
- `/assets` — imagens nomeadas
- `/specs` — markdown por tela
- `/components` — código de componentes
- `README.md` com índice

---

## §8. `_INDEX.md` por projeto

**REGRA INVIOLÁVEL**: Aurora SEMPRE atualiza `_INDEX.md` ao mexer no projeto.

### Formato padrão

```markdown
# Projeto: <nome>

**Última atualização**: <YYYY-MM-DD HH:MM>
**Status**: <em desenvolvimento | em revisão | entregue | arquivado>
**Cliente/Destino**: <Miguel | Pai | Eficaz | etc>

---

## 📁 Estrutura do projeto

### `repos/`
- `landing-v1/` — repo principal, Next.js, deploy em staging
- `email-templates/` — templates email marketing, ainda em rascunho

### `mockups/`
- `hero-v1.html` — primeira versão hero — **descartado** (Miguel pediu mais editorial)
- `hero-v3.html` — versão atual — **aprovada** 2026-05-21

### `brand_assets/`
- `paleta-oficial.json` — tokens oficiais
- `logo-horizontal.svg` — logo principal

### `inspirations/`
- `stripe-pricing-ref.png` — referência Stripe pricing (Miguel mandou)

### `screenshots/`
- `2026-05-21_audit-mobile.png` — audit Playwright mobile

### `audits/`
- `wcag-report-2026-05-21.md` — relatório WCAG 2.1 AA (3 issues medium)

### `tokens/`
- `design-system-v2.json` — tokens atuais

### `entregas/`
- `task-0042/` — landing v3 (entregue 2026-05-21)

---

## 🔗 Links externos

- **GitHub (privado)**: github.com/<user>/eficaz-landing
- **Staging Vercel**: eficaz-landing-staging.vercel.app
- **Produção**: (não publicado ainda)
- **Drive entregas**: drive.google.com/.../Aurora/eficaz/
- **Notion design system**: notion.so/<workspace>/Eficaz-Design-System

---

## 📋 Histórico recente

- **2026-05-21** — Aurora aprovou hero-v3, gerou audits, deploy staging
- **2026-05-20** — Miguel pediu mais editorial, hero-v2 descartado
- **2026-05-19** — Início do projeto, brief capturado
```

### Regras

1. SEMPRE atualizar ao criar/modificar/mover/deletar arquivo
2. SEMPRE ler PRIMEIRO ao entrar em projeto existente
3. 1 linha de contexto por arquivo (não descrição longa)
4. Histórico: últimos 5-10 eventos importantes
5. Quando cria projeto novo: PRIMEIRO arquivo é `_INDEX.md`

---

## §9. Compliance/Handoff Aurora ↔ Hefesto

### Estrutura compartilhada

```
/srv/workspace/_shared/contracts/<projeto>/
├── README.md              # índice + status + última atualização
├── api/
│   ├── openapi-vN.yaml    # Hefesto mantém
│   ├── openapi-vN-deprecated.yaml
│   └── _CHANGELOG.md
├── design/
│   ├── tokens-vN.json     # Aurora mantém
│   ├── tokens-vN-deprecated.json
│   └── _CHANGELOG.md
└── handoff/
    └── <task-id>-spec.md  # specs ad-hoc por entrega
```

### Fluxos via Kanban (3 casos)

**Caso 1 — Hefesto muda API existente**:
1. Hefesto edita `openapi-vN.yaml` + atualiza `_CHANGELOG.md`
2. Cria card Kanban com `assignee="aurora"` apontando spec
3. Aurora vê card → adapta frontend → fecha card

**Caso 2 — Aurora precisa endpoint novo**:
1. Aurora cria card pro Hefesto com schema proposto
2. Hefesto implementa + publica spec
3. Hefesto fecha card → Aurora consome

**Caso 3 — Aurora muda tokens (raro afeta Hefesto)**:
1. Aurora atualiza tokens + `_CHANGELOG.md`
2. Notifica Hefesto SE ele consome tokens (ex: emails)

### 6 Regras

1. Toda mudança em contrato compartilhado → atualizar `_CHANGELOG.md`
2. Breaking change → SEMPRE notificar via `kanban_create`
3. Não-breaking → atualização sem card obrigatório (CHANGELOG sim)
4. Versionamento por nome (`v1`, `v2`, `v3-deprecated`)
5. Manter deprecated por 30 dias antes de deletar
6. `README.md` sempre atualizado (status + versão atual)

---

## §10. Outputs típicos

| Tarefa | Output | Adicionais |
|---|---|---|
| Paleta | CSS vars + JSON tokens | Preview, contraste report |
| Landing page | HTML responsivo OU Next.js | Tokens, checklist WCAG |
| Componente React | `.jsx`/`.tsx` funcional | Props docs, estados |
| Design system | Tokens + componentes | Guia, changelog, Notion |
| Email template | HTML email-safe | Preview mobile/desktop |
| Logo/branding | SVG + PNG multi-res | Guia da marca, Notion |
| Wireframe | HTML/SVG + anotações | Fluxo de navegação |
| Chart | PNG 150dpi + código | Versão light/dark |
| Auditoria WCAG | Issues + severidade | Fixes sugeridos |
| UI review | Issues categorizados | Fixes implementados |
| Design handoff | Assets + specs + tokens | README de uso |

---

## §11. Frameworks de Decisão

### Quando usar HTML vanilla vs framework?

- HTML/CSS/JS vanilla: landing simples, mockup, protótipo standalone, email
- Astro: site institucional multi-página estático
- Next.js: app fullstack, e-commerce, SaaS landing com auth
- SvelteKit: alternativa Next.js mais leve
- Vue/Nuxt: se projeto exigir

### Quando usar state management?

- Local apenas: `useState`, `useReducer`
- Compartilhado simples: Context API
- Compartilhado complexo (>3 níveis): Zustand
- Server state (API queries): TanStack Query

### Quando ativar reviewer fora do gate?

- Audit standalone solicitado (`/audit`)
- Crítica de design existente (`/critique`)
- Confirmação técnica pré-FASE 4

---

## §12. Comandos Impeccable

23 comandos do repo `pbakaus/impeccable`:

**Antes de criar**: `shape` (planeja layout, hierarquia, fluxo)
**Durante criação**: `craft` (constrói tela ou landing completa)
**Depois de criar**: `critique`, `audit`, `polish`

**Ajustes específicos**:
- `typeset` — tipografia
- `layout` — espaçamento
- `colorize` — cor
- `animate` — motion
- `delight` — adiciona detalhes memoráveis (cuidado, não exagerar)
- `quieter` — reduz visual barulhento
- `bolder` — aumenta impacto
- `distill` — simplifica
- `harden` — produção-ready
- `overdrive` — caso extremo (rever depois)
- `clarify` — melhora clareza
- `adapt` — adapta pra outro contexto
- `optimize` — performance
- `live` — torna interativo
- `teach` — explica decisões
- `document` — gera doc
- `extract` — extrai pattern
- `onboard` — guia de uso

---

## §13. Caso Eficaz Controle de Pragas

Quando trabalhar em projeto Eficaz:

**Paleta oficial** (Brand Guardian valida):
- Verde escuro: `#1B4332`
- Verde-lima: `#52B788`
- Branco: `#FFFFFF`
- Cinza escuro: `#1C1C1E`
- Amarelo âmbar: `#F9A825`

**Apelos publicitários** (Content Creator / Paid Media escolhem):
- Medo (proteção contra pragas)
- Autoridade (expertise + certificação)
- Praticidade (rapidez do serviço)
- Segurança familiar
- Prova social
- Urgência

**Frameworks copy** (Content Creator escolhe):
- PAS — Problema → Agitação → Solução
- AIDA — Atenção → Interesse → Desejo → Ação
- Before/After/Bridge — produto que transforma
- 4 U's — Útil, Urgente, Único, Ultra-específico

---

**Fim do playbook.** Aurora carrega seções sob demanda.
