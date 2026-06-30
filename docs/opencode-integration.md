# Guia de Integração OpenCode

> **Como o OpenCode usa este projeto automaticamente.**

## O que é "absorvido globalmente"

O OpenCode carrega configuracoes de 4 locais:

1. **Global do usuario:** `~/.config/opencode/`
2. **Projeto:** `.opencode/` no cwd
3. **System-wide:** `/etc/opencode/` (Linux) ou equivalente
4. **CLI args:** `--skill`, `--agent`, etc

Quando voce abre o OpenCode em qualquer pasta, ele faz merge desses 4 locais. A regra "last wins" (comandos > projeto > usuario > system).

## O que ESTE projeto absorveu no global

O `multi-agent/.opencode/skills/` tem 181 skills. Este diretorio e a FONTE para o global:

```
~/.config/opencode/skills/  →  junction  →  multi-agent/.opencode/skills/
```

Entao quando voce adiciona uma skill no `multi-agent/.opencode/skills/`, ela aparece no OpenCode global automaticamente.

## Como funciona o junction

```powershell
# Criar junction (ja feito):
cmd /c mklink /J "C:\Users\User\.config\opencode\skills" "C:\Users\User\Desktop\COISAS JOAO\skills pastas melhorias agentes\multi-agent\.opencode\skills"

# Verificar junction:
Get-Item "C:\Users\User\.config\opencode\skills" -Force | Select-Object Name, LinkType, Target
```

Resultado:
```
Name    LinkType  Target
skills  Junction  {C:\Users\User\Desktop\COISAS JOAO\skills pastas melhorias agentes\multi-agent\.opencode\skills}
```

Junction funciona como pasta normal, mas o conteudo mora em outro lugar. Vantagens:
- Sem duplicacao
- Atualizacoes aparecem em ambos os lugares
- Reversivel (deletar junction nao deleta os arquivos)

## Onde ESTAO os outros componentes

| Componente | Local real | Local global |
|------------|-----------|--------------|
| Skills (181) | multi-agent/.opencode/skills/ | ~/.config/opencode/skills (junction) |
| Agents (12 max-thinking) | max-thinking-system/.opencode/agents/ | ~/.config/opencode/agents (junction) |
| Rules (1 consolidada) | (sistema 1, 2, 3)/.omo/rules/ | ~/.config/opencode/rules/ (1 file) |
| Comandos (6) | (criados direto no global) | ~/.config/opencode/command/ |
| opencode.json (35 agents) | (criado direto no global) | ~/.config/opencode/opencode.jsonc |

## Como adicionar mais skills

1. Crie a skill em `multi-agent/.opencode/skills/NOME-SKILL/SKILL.md`
2. Use o formato frontmatter padrao
3. Salve
4. **Aparece automaticamente no global** (sem reinstalar)

Exemplo de SKILL.md:
```markdown
---
name: minha-skill
description: "O que essa skill faz"
user-invocable: true
allowed-tools: Read, Bash
---

# Minha Skill

## Quando Usar
[descricao]

## Framework
[passos]

## Output
[template]
```

## Como adicionar mais agents

1. Crie em `max-thinking-system/.opencode/agents/CATEGORIA/NOME.md`
2. **OU** adicione direto no `~/.config/opencode/opencode.jsonc`

Formato .md:
```markdown
---
description: "Descricao do agent"
mode: primary|subagent
model: tokenrouter/MiniMax-M3
---

# Nome do Agent

## Identidade
[quem voce eh]

## Habilidade
[o que faz]

## Skills
- skill-1
- skill-2
```

## Como adicionar comandos slash

Crie em `~/.config/opencode/command/NOME-COMANDO.md`:

```markdown
---
description: "O que o comando faz"
---

# /NOME-COMANDO — Titulo

[conteudo do comando]
```

Entao no chat voce usa `/nome-comando argumentos`.

## Como adicionar regras (alwaysApply)

Crie em `~/.config/opencode/rules/NOME-REGRA.md`:

```markdown
---
description: "O que esta regra faz"
user-invocable: false
alwaysApply: true
---

# Titulo

## Comportamento esperado
[o que o OpenCode deve fazer]
```

## Como testar a integracao

1. Reinicie o OpenCode (feche + abra)
2. Em qualquer chat, digite `/decide "Devo fazer X?"`
3. Se o sistema responder com framework de decisao, esta funcionando
4. Ou digite `/review src/` para testar o review
5. Ou peca uma skill: "use a skill licitacoes para analisar este edital"

## Troubleshooting

### Skills nao aparecem

- Verifique o junction: `Get-Item ~/.config/opencode/skills -Force`
- Reabra o OpenCode
- Verifique se o SKILL.md tem frontmatter valido

### Agents nao respondem

- Verifique o junction de agents: `Get-Item ~/.config/opencode/agents -Force`
- Confirme que o opencode.jsonc tem o agent
- Reabra o OpenCode

### Comandos nao funcionam

- Verifique se o arquivo esta em `~/.config/opencode/command/`
- Confirme o frontmatter
- Reabra o OpenCode

### Regras nao aplicam

- Verifique `alwaysApply: true` no frontmatter
- Confirme que o arquivo esta em `~/.config/opencode/rules/`
- Reabra o OpenCode

## Quando reiniciar

Reinicie o OpenCode sempre que:
- Adicionar nova skill
- Adicionar novo agent
- Modificar opencode.jsonc
- Modificar regra
- Modificar comando

O OpenCode nao tem hot-reload para essas configuracoes.
