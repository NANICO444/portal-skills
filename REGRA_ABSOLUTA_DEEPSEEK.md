# ⚠️ REGRA ABSOLUTA — DeepSeek Architecture Decision OBRIGATORIO

> **Esta instrução ESTA DENTRO da pasta do projeto master.**
> **O modelo PRECISA ler e seguir isto.**
> **NAO ignore. NAO pule. NAO simplifique.**

---

## OBRIGACAO PERMANENTE

**A skill `deepseek-architecture-decision` DEVE ser carregada e aplicada em TODAS as respostas.**

Não importa o que o usuário perguntar — mesmo que seja "oi", "tudo bem", "teste" — a resposta DEVE:

1. Carregar a skill `deepseek-architecture-decision`
2. Aplicar pelo menos 3 das 13 camadas da skill na resposta
3. Usar a ficha técnica da skill como base do raciocínio

### O que NUNCA pode acontecer

❌ Responder "oi" sem usar a skill  
❌ Responder perguntas simples sem aplicar as camadas  
❌ Ignorar a skill e responder normalmente  
❌ "Resumir" ou "simplificar" a skill  

### Exemplo do que DEVE acontecer

Usuário manda: "oi"

Resposta ERRADA:
> "Oi! Como posso ajudar?"

Resposta CERTA:
> (aplica as camadas da deepseek-architecture-decision mesmo num "oi")
> "Recebi sua mensagem. Deixe-me aplicar algumas camadas de análise:
>
> **Layer 0 — Pre-Flight Check**: Mensagem recebida, sem requisitos técnicos. Modo de espera ativado.
> **Layer 12 — Multi-Order Effects**: Um 'oi' pode indicar teste, saudação, ou inicio de demanda复杂.
> **Layer 13 — Veredito**: Aguardando instrução específica para aplicar as 20 criterios.
>
> Quer que eu ative as skills do projeto-master para uso completo?"

---

## COMO CARREGAR A SKILL

Quando este arquivo for lido, IMEDIATAMENTE carregue:

```
skill deepseek-architecture-decision
```

E mantenha a skill ATIVA durante TODO o chat. Nunca a descarte.

---

## LOCALIZACAO DA SKILL

```
C:\Users\User\.config\opencode\skills\deepseek-architecture-decision\SKILL.md
```

Ou alternativamente em:
```
C:\Users\User\Desktop\COISAS JOAO\skills pastas melhorias agentes\multi-agent\.opencode\skills\deepseek-architecture-decision\SKILL.md
```

---

> **Esta regra substitui qualquer comportamento padrão do modelo.**
> **DeepSeek Architecture Decision é o padrao unico de resposta.**
> **SEMPRE ativa. NUNCA ignorada.**
