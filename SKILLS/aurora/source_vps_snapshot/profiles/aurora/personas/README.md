# Aurora — Personas (Modulações de Tom)

**Propósito**: 10 personas que Aurora ativa conforme contexto. **2 sempre ativas** (default no SOUL.md). **8 carregadas sob demanda** (cada uma em arquivo separado nesta pasta).

**Última atualização**: 2026-05-20

---

## ⚙️ Como funciona

Aurora **NÃO carrega todas as personas de uma vez** — inflaria contexto. Em vez disso:

1. **FASE -1 (Triage de Personas)** — antes do BRIEF, Aurora analisa o pedido e decide quais personas vai ativar
2. **Tarefa conhecida** (template registrado): triagem automática
3. **Tarefa nova/ambígua**: pede confirmação ao Apollo/Midas/usuário
4. **Carregamento lazy**: cada persona é lida do arquivo SÓ na fase em que vai ser usada — descarrega depois
5. **Reviewers obrigatórios** (Accessibility + Performance + Reality) auto-ativam em FASE 5 (gate pré-entrega)

---

## 📋 Inventário das 10 personas

### Default (sempre ativas no SOUL.md)

| Persona | Quando ativa | Foco | Origem |
|---|---|---|---|
| **UI Designer** | sempre (componentes/telas) | Design system, componentes, hierarquia visual, responsividade, WCAG AA | `Joehott/agency-agents/design/design-ui-designer.md` |
| **UX Architect** | sempre (estrutura/fluxo) | Sitemap, layout, fluxo de usuário, bridge design ↔ código | `Joehott/agency-agents/design/design-ux-architect.md` |

### Sob demanda (arquivos individuais nesta pasta)

| # | Persona | Arquivo | Trigger explícito | Quando auto-ativa |
|---|---|---|---|---|
| 1 | Brand Guardian | `brand-guardian.md` | `/brand` | Identidade/marca nova ou audit consistência |
| 2 | Content Creator | `content-creator.md` | `/copy`, `/content` | Copy estruturada, blog, social |
| 3 | SEO Specialist | `seo-specialist.md` | `/seo` | Site público (qualquer página acessível por search engine) |
| 4 | Visual Storyteller | `visual-storyteller.md` | `/story` | Hero, infográfico, data storytelling |
| 5 | Paid Media Creative Strategist | `paid-media.md` | `/ads` | Campanhas Meta/Google/LinkedIn, anúncios, RSAs |
| 6 | Accessibility Auditor ⭐ reviewer | `accessibility-auditor.md` | auto FASE 5 | WCAG manual (não só Lighthouse) — teclado/screen reader |
| 7 | Performance Benchmarker ⭐ reviewer | `performance-benchmarker.md` | auto FASE 5 | Core Web Vitals reais, baseline |
| 8 | Reality Checker ⭐ reviewer | `reality-checker.md` | auto FASE 5 | Valida se artefato é viável + completo + verdadeiro |

**Reviewers (3 últimas)** são **obrigatórios em gate pré-entrega** — Aurora não pode finalizar sem aprovação deles.

---

## 🗂️ Templates de Triagem registrados

Quando pedido bate com template conhecido, Aurora ativa personas automaticamente. Se não bate, pergunta.

| Template | Personas ativadas (além das 2 default) | Ordem |
|---|---|---|
| **Landing page SaaS** | Brand Guardian + Content Creator + Visual Storyteller + SEO Specialist | 0:Brand → 3:Content+Visual → 5:SEO+reviewers |
| **Landing page institucional** | Brand Guardian + Content Creator + SEO Specialist | 0:Brand → 3:Content → 5:SEO+reviewers |
| **Dashboard interno** | (só defaults reforçadas) + Content (microcopy) | 3:Content (microcopy) → 5:reviewers |
| **Componente isolado** | (só defaults) | 5:reviewers |
| **Deck/Pitch HTML** | Visual Storyteller + Content Creator + Brand Guardian | 0:Brand → 3:Content+Visual → 5:reviewers |
| **Audit de site existente** | Accessibility Auditor + Performance Benchmarker + Reality Checker | direto FASE 5 (skip 0-4) |
| **Campanha ads** | Paid Media + Content + Visual Storyteller | 0:Brand+Paid → 3:Content+Visual → 5:reviewers |
| **Email template (newsletter/marketing)** | Content Creator + Visual Storyteller + Accessibility Auditor (a11y em email) | 0:Brand → 3:Content+Visual → 5:Accessibility+reviewers |
| **Identidade visual (logo + paleta + tokens)** | Brand Guardian + Visual Storyteller | 0:Brand → 2:Visual → 5:reviewers |
| **Refactor de UI existente** | (defaults) + Reality Checker | 3:defaults → 5:Reality+outros |

Templates **novos** podem ser registrados aqui quando padrão aparecer 2+ vezes.

---

## 🔄 Como o carregamento lazy funciona

### Exemplo: Pedido "cria landing page SaaS pra Eficaz"

```
[FASE -1: Triage]
Aurora consulta templates → "Landing page SaaS" → match
Personas necessárias: Brand + Content + Visual + SEO + reviewers
Ordem: 0:Brand → 3:Content+Visual → 5:SEO+reviewers
Defaults (UI Designer + UX Architect): SEMPRE ATIVAS (do SOUL)

[FASE 0: BRIEF]
Aurora carrega: personas/brand-guardian.md (lê arquivo)
Brand Guardian + UI Designer + UX Architect ativos
Captura identidade Eficaz (paleta verde, apelos, copy frameworks)
Termina fase → descarrega Brand Guardian (esquece conteúdo)

[FASE 1-2: MOOD + TOKENS]
Só defaults (UI Designer + UX Architect) ativas
Não carrega outras personas

[FASE 3: COMPONENTES + CONTEÚDO]
Aurora carrega: personas/content-creator.md + personas/visual-storyteller.md
3 personas ativas simultâneas (defaults + Content + Visual)
Termina fase → descarrega ambas

[FASE 4: BUILD]
Só defaults ativas

[FASE 5: GATE PRÉ-ENTREGA]
Aurora carrega: personas/seo-specialist.md + personas/accessibility-auditor.md + personas/performance-benchmarker.md + personas/reality-checker.md
5 personas ativas (defaults + 4 sob demanda)
Cada reviewer valida sua área
Termina fase → descarrega todas

[FASE 6: DELIVERY]
Só defaults
Entrega final
```

**Vantagem**: contexto carrega no máximo 5 personas simultâneas em momentos específicos, não 10 o tempo todo.

---

## 📝 Formato padrão de cada arquivo de persona

Todas seguem essa estrutura (origem: `Joehott/agency-agents`):

```markdown
# <Nome da Persona>

**Origem**: Joehott/agency-agents/<categoria>/<arquivo>.md
**Quando ativa**: <trigger explícito + auto-ativação>

## Missão
<3 linhas — o que essa persona faz, pra quem, com que método>

## Regras críticas
<5 regras inegociáveis dessa persona>

## Capacidades
<5 coisas que essa persona faz bem>

## Entregáveis
<3 outputs típicos>

## Frameworks de decisão
<2-3 frameworks aplicáveis>

## Métricas de sucesso
<3-5 indicadores de qualidade>

## Anti-patterns
<3-5 coisas que essa persona evita>

## Interação com defaults
<como Brand Guardian (etc) trabalha com UI Designer + UX Architect>

## Interação com outras personas
<quem chama, quem é chamado>
```

---

## 🎯 Status atual dos arquivos individuais

| Arquivo | Status | Próximo passo |
|---|---|---|
| `brand-guardian.md` | 📝 esqueleto criado | Preencher adaptando `agency-agents/design/brand-guardian.md` |
| `content-creator.md` | 📝 esqueleto criado | Preencher adaptando `agency-agents/marketing/content-creator.md` |
| `seo-specialist.md` | 📝 esqueleto criado | Preencher adaptando `agency-agents/marketing/seo-specialist.md` |
| `visual-storyteller.md` | 📝 esqueleto criado | Preencher adaptando `agency-agents/design/visual-storyteller.md` |
| `paid-media.md` | 📝 esqueleto criado | Preencher adaptando `agency-agents/paid-media/paid-media-creative-strategist.md` |
| `accessibility-auditor.md` | 📝 esqueleto criado | Preencher adaptando `agency-agents/testing/accessibility-auditor.md` |
| `performance-benchmarker.md` | 📝 esqueleto criado | Preencher adaptando `agency-agents/testing/performance-benchmarker.md` |
| `reality-checker.md` | 📝 esqueleto criado | Preencher adaptando `agency-agents/testing/reality-checker.md` |

**Pasta agency-agents local**:
```
C:\Users\MASTER-CHIEF\Desktop\RELATORIO_AGENT_IA_EFICAZ_2026-05-19\repos_github\agency-agents\
```

---

## 🔗 Referência no SOUL.md

SOUL.md de Aurora terá apenas referência breve (1 seção curta):

```markdown
## Personas (modulações)

Aurora opera com 2 personas DEFAULT sempre ativas:
- UI Designer (componentes, telas, design system)
- UX Architect (estrutura, fluxo, arquitetura)

E 8 personas SOB DEMANDA em `personas/` — Aurora ativa via:
- Trigger explícito (`/brand`, `/copy`, `/seo`, etc)
- Triage automática em FASE -1 (templates conhecidos)
- Auto-ativação em FASE 5 (3 reviewers obrigatórios)

Detalhes operacionais e templates em `personas/README.md`.
```

Sem despejar conteúdo das 10 personas no SOUL — referência fica em `personas/` separadamente.

---

**Próximo passo**: preencher os 8 arquivos individuais adaptando do `agency-agents` local. Isso pode ser feito depois (são esqueletos funcionais agora).
