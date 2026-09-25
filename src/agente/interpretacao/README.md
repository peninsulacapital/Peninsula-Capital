# interpretacao
**Papel:** primeira etapa do pipeline. Traduz "cegamente" o texto livre do cliente em dados operáveis — sem julgar se está completo ou coerente (isso é `validacao`).

**Entra:** texto em português (`inputs/casos/`, ou a resposta do cliente a uma pergunta de esclarecimento). **Sai:** o objeto de perfil definido em `schemas`.

**Não vai aqui:** julgamento sobre o que o cliente disse (isso é `validacao`), nem conta de qualquer tipo.

**Regra dura:** o que o cliente não disse fica marcado como ausente. Nunca preencher por inferência.

**Registra declarações, não classificações:** o que o cliente disse sobre risco, prazos ou valores entra como foi dito, com o trecho literal de origem. Consolidar em perfil de risco é `validacao`; fazer conta é `financeiro`.

**O que extrair:** `ClientProfile`, em `schemas/client_profile.py`.

**A observar:** jargão financeiro pode parecer ambíguo ao LLM sem ser (ex.: "4% em termos reais" = 4% acima da inflação). Por ora vira status `ambiguous` e `validacao` pergunta; se essas perguntas ficarem frequentes demais, buscar alternativa.

**Loop com `validacao`:** quando `validacao` devolve uma pergunta de esclarecimento e o cliente responde, a resposta passa de novo por `interpretacao` antes de voltar a `validacao`.

**Natureza:** LLM, com prompts revisados por vocês. **Estado:** vazio.
