# interpretacao
**Papel:** primeira etapa do pipeline. Traduz "cegamente" o texto livre do cliente em dados operáveis — sem julgar se está completo ou coerente (isso é `validacao`).

**Entra:** texto em português (`inputs/casos/`, ou a resposta do cliente a uma pergunta de esclarecimento). **Sai:** o objeto de perfil definido em `schemas`.

**Não vai aqui:** julgamento sobre o que o cliente disse (isso é `validacao`), nem conta de qualquer tipo.

**Regra dura:** o que o cliente não disse fica marcado como ausente. Nunca preencher por inferência.

**Loop com `validacao`:** quando `validacao` devolve uma pergunta de esclarecimento e o cliente responde, a resposta passa de novo por `interpretacao` antes de voltar a `validacao`.

**Natureza:** LLM, com prompts revisados por vocês. **Estado:** vazio.
