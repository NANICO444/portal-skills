# Hooks do Nexus OS

Gatilhos manuais opcionais para quality gates.

## Como usar
1. Edite o arquivo `.kiro/hooks/nexus-quality-gate.kiro.hook`
2. Mude `"enabled": false` para `"enabled": true`
3. O OpenCode/Kiro IDE oferecerá o gate manualmente quando solicitado

## Hooks disponíveis
- `nexus-quality-gate` — revisão final: testes, diff, segurança, verificação visual, riscos

> Nota: Os hooks originais do Hefesto e Aurora foram substituídos por este único hook unificado.
