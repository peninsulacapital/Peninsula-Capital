# agente
O código, dividido em caixas. Duas famílias:

**Caixas do pipeline** (cada uma recebe e devolve objetos de `schemas`):

`interpretacao` ⇄ `validacao` → `financeiro` ⇄ `analista` → `relatorio`

- `interpretacao` ⇄ `validacao`: entender o cliente, com perguntas de esclarecimento até o perfil fechar.
- `financeiro` ⇄ `analista`: `financeiro` entrega diagnóstico e cardápio de carteiras; `analista` decide e, se precisar de um número a mais, pede um cálculo.
- `relatorio`: só apresenta.

**Infraestrutura transversal** (usada por várias caixas, não é etapa com posição fixa):

`schemas` (contrato de dados), `mercado` (premissas de mercado: Excel da banca + config), `llm` (acesso ao modelo), `prompts` (textos enviados ao modelo).

`mercado` não depende do cliente — só de dados e premissas — por isso não tem lugar fixo na esteira: `financeiro` a consulta quando precisa.

`orquestrador.py` é o único lugar que conhece a ordem das etapas e conduz os dois loops; nenhuma caixa chama outra diretamente.

**Estado:** `schemas` com o perfil do cliente; demais vazias. Construção bottom-up, uma caixa por vez.
