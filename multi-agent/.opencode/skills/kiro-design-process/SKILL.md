---
name: kiro-design-process
description: "Processo de Design Aurora — 6 passos: brief, pesquisar, criar, refinar, verificar, entregar"
argument-hint: "[descrição da tarefa de design/UX]"
user-invocable: true
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, Task, WebFetch
agent: orquestrador
---

# Processo de Design (Aurora)

Metodologia de design visual e experiência do usuário em 6 passos.

## Princípios Base
- **Clareza visual** — informações hierarquizadas, espaçamento generoso
- **Consistência** — cores, tipografia, espaçamentos seguem sistema
- **Responsividade** — funciona em mobile, tablet, desktop
- **Acessibilidade** — contraste, foco visível, labels, navegação
- **Acabamento** — micro-interações, transições sutis, estados vazios

## Fluxo Obrigatório

### Passo 1 — Briefing
- Entenda objetivo da interface (o que o usuário DEVE conseguir fazer?)
- Público-alvo: poder aquisitivo, faixa etária, contexto de uso
- Restrições: identidade visual existente, componentes reutilizáveis
- Referências: sites/UI que o usuário gosta (peça exemplos)

### Passo 2 — Pesquise e Planeje
- Consulte `skill:design-brief` para estruturar o levantamento
- Identifique padrões de UI para o tipo de interface (dashboard, landing, formulário, etc.)
- Documente decisões de layout antes de codificar
- Use `skill:excalidraw` para wireframes rápidos (se complexo)

### Passo 3 — Crie a Interface
- Hierarquia visual clara: título > subtítulo > ação > detalhes
- Paleta de cores: `skill:palette` para gerar esquema consistente
- Tipografia: contraste, legibilidade, hierarquia
- Componentes reutilizáveis: `skill:component-library`
- Estados: carregando, vazio, erro, sucesso, hover, focus, active

### Passo 4 — Refine
- Animações e transições: `skill:motion-foundations`
- Responsividade: teste em 3 breakpoints (mobile 375px, tablet 768px, desktop 1280px)
- Acessibilidade: navegação por teclado, foco visível, contraste WCAG AA
- Micro-cópias: botões, labels, mensagens de erro, placeholders

### Passo 5 — Verifique
- Checklist de acessibilidade:
  - [ ] Contraste 4.5:1 (texto normal), 3:1 (texto grande)
  - [ ] Foco visível em todos os elementos interativos
  - [ ] Labels associados a inputs
  - [ ] Navegação por tab ordenada e lógica
  - [ ] `role` e `aria-*` corretos
- Checklist de responsividade:
  - [ ] Não quebra em mobile
  - [ ] Touch targets ≥ 44px
  - [ ] Scroll horizontal inexistente
  - [ ] Fontes legíveis sem zoom
- Checklist de performance:
  - [ ] Imagens otimizadas
  - [ ] CSS sem duplicação
  - [ ] JS carregado sob demanda

### Passo 6 — Entregue
- Preview funcional (não screenshot)
- Lista de componentes criados/modificados
- Notas de decisão de design (por que escolheu X em vez de Y)
- Recomendações para próximas iterações

## Regras de Ouro

✅ Menos é mais: cada elemento precisa se justificar.
✅ Componentes reutilizáveis primeiro: depois componha a página.
✅ Acessibilidade não é opcional: é requisito.
✅ Consistência > criatividade: siga o sistema existente.

❌ Animações que atrasam a interação.
❌ Cores sem contraste suficiente.
❌ Assumir resolução/viewport do usuário.
❌ "Melhorar" design existente sem necessidade.
