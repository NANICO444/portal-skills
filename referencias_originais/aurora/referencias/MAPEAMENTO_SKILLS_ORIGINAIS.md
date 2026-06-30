# Mapeamento Das Skills Originais Para Kiro IDE

## Como Ler Este Mapa

O arquivo original `skills_list.md` descreve capacidades para Hermes, nao pacotes Kiro prontos. Esta adaptacao nao finge instalar ferramentas externas. Ela converte os comportamentos necessarios em skills de workspace compatíveis com o Kiro IDE.

Ha uma inconsistencia no inventario original: o titulo declara `39 skills`, mas inclui 19 universais e uma tabela visual numerada ate 23, com uma linha que agrupa duas skills de movimento. Por isso, o pacote cobre **capacidades declaradas**, em vez de prometer uma contagem Hermes identica.

## Capacidades Universais

| Original | Adaptacao Kiro | Estado |
|---|---|---|
| `tavily-search` | `aurora-research-verify` + ferramenta web disponivel no Kiro | Adaptado, sem exigir chave Tavily |
| `web-fetch` | ferramentas web do Kiro quando disponiveis | Nativo do ambiente, nao duplicado |
| `web-scrape` | ferramentas web do Kiro quando disponiveis | Nativo do ambiente, nao duplicado |
| `doc-cache` | leitura e documentacao local do workspace | Simplificado |
| `doc-read` | leitura de arquivos do Kiro | Nativo do ambiente |
| `ocr` | nao presumido; usar apenas ferramenta instalada no projeto | Opcional |
| `maton-gateway` | removido como requisito; integracoes so com autorizacao | Adaptado ao PC local |
| `factual-verify` | `aurora-research-verify` | Incluido |
| `verification-before-completion` | `aurora-testing`, `aurora-reality-check`, `aurora-delivery` | Incluido |
| `anti-glaze` | `aurora-visual-qa`, `aurora-interface-polish` | Incluido |
| `karpathy-discipline` | `AGENTS.md`, `aurora-fullstack-feature` | Incorporado |
| `find-skills` | importacao de skills pelo painel Kiro, se solicitada | Nao obrigatorio |
| `token-budget-advisor` | skills curtas carregadas sob demanda | Incorporado |
| `council` | `aurora-mood-directions` + escolha do usuario | Substituido |
| `documentation-lookup` | `aurora-research-verify`, `aurora-documentation` | Incluido |
| `duckduckgo-search` | web do Kiro quando disponivel | Nao duplicado |
| `native-mcp` | Powers/MCP do Kiro somente se o usuario instalar | Opcional |
| `critical-thinking` | `AGENTS.md`, `aurora-reality-check` | Incluido |
| `human-in-the-loop` | regras de confirmacao em `AGENTS.md` e steering | Incluido |

## Capacidades Especificas De Aurora

| Original | Adaptacao Kiro | Estado |
|---|---|---|
| `impeccable` | `aurora-visual-qa`, `aurora-interface-polish` | Comportamento adaptado; pacote externo nao copiado |
| `palette` | `aurora-design-tokens` | Incluido |
| `component-library` | `aurora-component-library` | Incluido |
| `content-generation` | `aurora-content-creator` | Incluido |
| `accessibility-audit` | `aurora-accessibility-audit` | Incluido |
| `frontend-stack-decision` | `aurora-frontend-build`, `aurora-fullstack-feature` | Incluido |
| `performance-web-vitals` | `aurora-performance-audit` | Incluido |
| `browser-testing` | `aurora-visual-qa`, `aurora-testing` | Incluido |
| `design-md` | `aurora-design-tokens`, `aurora-documentation` | Incluido |
| `design-brief` | `aurora-design-brief` | Incluido |
| `seo-advanced` | `aurora-seo-content` | Incluido |
| `api-integration` | `aurora-api-integration` | Incluido e expandido |
| `deploy-protocol` | `aurora-deploy-preview` | Incluido, exige confirmacao externa |
| `error-recovery-design` | `aurora-error-recovery` | Incluido |
| `html-anything` | `aurora-frontend-build`, `aurora-wireframe` | Capacidade adaptada; templates externos nao copiados |
| `popular-web-designs` | `aurora-mood-directions`, `aurora-research-verify` | Incluido como processo |
| `design-extract` | `aurora-design-extraction` | Incluido |
| `baoyu-infographic` | `aurora-infographic` | Incluido como processo |
| `frontend-patterns` | `aurora-frontend-patterns` | Incluido |
| `react-doctor` | `aurora-debugging`; CLI externa apenas se usuario aprovar | Adaptado |
| `motion-foundations` e `motion-patterns` | `aurora-motion-polish` | Incluido |
| `excalidraw` | `aurora-wireframe`; integracao externa nao presumida | Adaptado |
| `make-interfaces-feel-better` | `aurora-interface-polish` | Incluido |

## Novas Capacidades Necessarias

Como Aurora agora trabalha sozinha e pode programar o necessario, o pacote adiciona:

| Skill Kiro | Motivo |
|---|---|
| `aurora-fullstack-feature` | Substitui a dependencia de outro agente para backend e logica. |
| `aurora-testing` | Exige verificacao real de comportamento. |
| `aurora-debugging` | Permite investigar falhas ponta a ponta. |
| `aurora-security-boundaries` | Protege segredos, dados e operacoes sensiveis. |
| `aurora-reality-check` | Evita declarar entrega sem evidencia. |
| `aurora-documentation` | Mantem uso e decisoes claras no workspace local. |

## Nao Incluido Como Requisito

- Comandos `hermes -p aurora ...`.
- Pastas `~/.hermes`.
- Maton, contas externas ou deploy automatico.
- Conectores, MCPs ou Powers que nao estejam instalados e autorizados no Kiro.
- Conteudo integral de skills de terceiros; o pacote contem instrucoes adaptadas proprias.
