---
name: kiro-verification
description: "Checklist de verificação e entrega — obrigatório antes de declarar uma tarefa pronta"
argument-hint: "[tarefa a verificar antes de entregar]"
user-invocable: true
allowed-tools: Read, Bash, Grep
agent: orquestrador
---

# Verificação e Entrega

Checklist obrigatório ANTES de dizer "pronto", "feito", "funciona" ou "entregue".

## Verificação Técnica

### Build & Compilação
- [ ] Código compila SEM warnings novos
- [ ] Build passa em modo produção (não só dev)
- [ ] Sem dependências faltando
- [ ] Sem dependências não utilizadas (limpas)

### Testes
- [ ] Todos os testes existentes passam
- [ ] Testes novos cobrem a mudança
- [ ] Cobertura não diminuiu
- [ ] Testes de borda (edge cases) cobertos
- [ ] Testes de regressão para bugs corrigidos

### Lint & Type Check
- [ ] Linter passa sem warnings novos
- [ ] Type check (TypeScript/mypy) passa
- [ ] Formatação consistente (prettier/black)
- [ ] Sem TODOs antigos abandonados

### Verificação Manual
- [ ] Funcionalidade testada em ambiente real (não só "deveria funcionar")
- [ ] Screenshots/gravações de comportamento (se UI)
- [ ] Logs limpos durante execução
- [ ] Performance aceitável (não introduziu lentidão)

## Verificação de Qualidade

### Código
- [ ] Não duplica lógica existente
- [ ] Nomes claros e descritivos
- [ ] Comentários explicam POR QUÊ (não o quê)
- [ ] Sem código morto (variáveis não usadas, imports órfãos)
- [ ] Tratamento de erros adequado

### Segurança
- [ ] Sem credenciais hardcoded
- [ ] Sem logs de dados sensíveis
- [ ] Inputs validados
- [ ] Autenticação/autorização verificadas
- [ ] Rate limiting em endpoints públicos

### Compatibilidade
- [ ] Não quebra funcionalidade existente
- [ ] Migração de dados documentada (se houver)
- [ ] Mudanças de API versionadas
- [ ] Feature flags usadas (se mudança grande)

## Verificação de UX (se UI)

### Visual
- [ ] Renderiza em mobile, tablet, desktop
- [ ] Estados cobertos: loading, vazio, erro, sucesso
- [ ] Foco visível em todos elementos interativos
- [ ] Hover/active states implementados
- [ ] Acessibilidade WCAG AA

### Interação
- [ ] Formulários: validação em tempo real
- [ ] Botões: feedback visual ao clicar
- [ ] Navegação por teclado funcional
- [ ] Mensagens de erro claras e acionáveis
- [ ] Loading states para operações lentas

## Verificação de Documentação

### Atualizada
- [ ] README atualizado (se interface)
- [ ] CHANGELOG atualizado
- [ ] Comentários inline atualizados
- [ ] OpenAPI/Swagger atualizada (se API)
- [ ] ADRs criados para decisões importantes

### Acessível
- [ ] Exemplos de uso funcionais
- [ ] Pré-requisitos listados
- [ ] Instruções de setup claras
- [ ] Troubleshooting documentado

## Entrega

### Comunicação
- [ ] Resumo de mudanças em 1-2 frases
- [ ] Lista de arquivos alterados
- [ ] Evidências (logs de teste, screenshots, comandos rodados)
- [ ] Riscos residuais conhecidos
- [ ] Próximos passos sugeridos (se aplicável)

### Repositório
- [ ] Branch correto
- [ ] Commits atômicos e bem descritos
- [ ] PR aberto com descrição completa
- [ ] Reviewers designados
- [ ] CI/CD passou

## Regras de Ouro

✅ "Funciona" só se TESTOU funcionando, não se "deveria funcionar".
✅ Liste TUDO que mudou, não só o que o usuário pediu.
✅ Documente decisões não-óbvias (por que escolheu X).
✅ Se algo falhou, FALO que falhou — não escondo.

❌ "Pronto" sem testar.
❌ "100% testado" sem ver a saída dos testes.
❌ Pular checklist por "ser mudança pequena".
❌ Esconder bugs conhecidos para "resolver depois".
