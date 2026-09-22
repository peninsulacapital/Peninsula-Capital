# agente
O código, dividido em caixas. Duas famílias:

**Caixas do pipeline** (rodam em ordem, cada uma recebe e devolve objetos de `schemas`):

`interpretacao` → `validacao` → `financeiro` → `portfolio` → `relatorio`

**Infraestrutura transversal** (usada por várias caixas, não é etapa com posição fixa):

`schemas` (contrato de dados), `mercado` (premissas de mercado: Excel da banca + config), `llm` (acesso ao modelo), `prompts` (textos enviados ao modelo).

`mercado` não depende do cliente — só de dados e premissas — por isso não tem lugar fixo na esteira: `financeiro` e `portfolio` a consultam quando precisam.

`orquestrador.py` é o único lugar que conhece a ordem das etapas; nenhuma caixa chama outra diretamente.

**Estado:** todas vazias. Construção bottom-up, uma caixa por vez, começando pelo fornecimento de dados.
