# interpretacao
**Papel:** primeira etapa do pipeline. Traduz "cegamente" o texto livre do cliente em dados operáveis — sem julgar se está completo ou coerente (isso é `validacao`).

**Entra:** texto em português (`inputs/casos/`, ou a resposta do cliente a uma pergunta de esclarecimento). **Sai:** o objeto de perfil definido em `schemas`.

**Não vai aqui:** julgamento sobre o que o cliente disse (isso é `validacao`), nem conta de qualquer tipo.

**Regra dura:** o que o cliente não disse fica marcado como ausente. Nunca preencher por inferência.

**Loop com `validacao`:** quando `validacao` devolve uma pergunta de esclarecimento e o cliente responde, a resposta passa de novo por `interpretacao` antes de voltar a `validacao`.

**Natureza:** LLM, com prompts revisados por vocês. **Estado:** vazio.

## Regras de Inconsistência
- Se o cliente informar um patrimônio de alto risco, mas declarar zero tolerância a perdas, ou informar números que não batem, marcar o campo `alerta_inconsistencia = true`.
- Se faltarem dados essenciais para o cálculo, acionar o fluxo de validação (`validacao`).

## Variáveis Extraídas (Entidades)
- `patrimonio_total`: Valor financeiro informado.
- `caixa` : patrimonio líquido do cliente
- `renda` : valor o cliente ganha por ano
- `gastos` : valor que o cliente gasta por ano
- `objetivos`: Prazos e metas financeiras.
- `perfil_risco`: Conservador, Moderado ou Arrojado.
- `experiência` : histórico de investimentos do cliente.
