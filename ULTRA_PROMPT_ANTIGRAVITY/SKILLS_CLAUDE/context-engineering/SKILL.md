---
name: context-engineering
description: "Engenharia de contexto para LLMs: otimizacao de prompts, janela de contexto, recuperacao (RAG), compressao e gestao eficiente de informacao em sessoes longas. Use em projetos com grandes codebases ou muitas dependencias."
---

# SKILL: Context Engineering (Engenharia de Contexto)
# A técnica mais avançada de 2026 para maximizar a inteligência da IA

---

## O que é Context Engineering?
Em vez de apenas "conversar com a IA", você CONTROLA exatamente que informações
entram no contexto dela, em que formato, e com que prioridade.
Pense no modelo de IA como uma CPU e a janela de contexto como a RAM.

## Técnicas Avançadas

### 1. Bento-Box Prompting
Separe instruções de dados usando tags XML:
```xml
<task>
Crie uma landing page cyberpunk para o Nexus OS
</task>

<constraints>
- Usar apenas HTML/CSS/JS vanilla
- Paleta: cyan neon (#00f5ff) sobre preto (#050508)
- Mobile-first com breakpoints em 768px e 480px
</constraints>

<reference_code>
[Cole aqui o código existente que deve ser seguido como referência]
</reference_code>

<output_format>
Retorne o HTML completo, pronto para salvar como index.html
</output_format>
```

### 2. Chain of Thought Forçado
Para tarefas de lógica complexa, force o raciocínio passo a passo:
```
Antes de escrever QUALQUER código:
1. Liste os requisitos que você identificou
2. Descreva a arquitetura que vai usar e POR QUÊ
3. Identifique possíveis problemas
4. Só então comece a implementar
```

### 3. Few-Shot com Exemplos Reais
Em vez de descrever o que você quer, MOSTRE um exemplo:
```
Quero que você crie cards no estilo abaixo:

EXEMPLO (correto):
<div class="feature-card">
    <div class="card-icon">🛡️</div>
    <h3 class="card-title">Nível RPG</h3>
    <p class="card-text">Sistema de XP...</p>
</div>

Agora crie 3 cards novos seguindo EXATAMENTE este padrão.
```

### 4. Negative Prompting (O que NÃO fazer)
Tão importante quanto dizer o que quer é dizer o que NÃO quer:
```
NÃO faça:
- Não use Tailwind ou Bootstrap
- Não crie componentes React
- Não adicione comentários óbvios
- Não mude a estrutura de pastas existente
```

### 5. Memory Injection (Injeção de Memória)
Para sessões longas, injete um resumo compacto no início:
```
CONTEXTO DA SESSÃO:
- Projeto: Nexus OS (assistente IA desktop)
- Stack: Python + Tkinter (app) / HTML+CSS+JS (site)
- Status: Fase 1 completa, iniciando Fase 2
- Última ação: Corrigido bug do autoplay do rádio
```

## Quando Usar Esta Skill
- Antes de qualquer tarefa que envolva mais de 50 linhas de código
- Quando a IA está "desobedecendo" ou gerando respostas genéricas
- Quando você precisa de output EXATO num formato específico
- Quando está trabalhando com múltiplos arquivos interdependentes
