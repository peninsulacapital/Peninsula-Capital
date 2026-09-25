# analista
**Papel:** o juízo sobre o plano. Recebe os números prontos de `financeiro` e aplica as regras de decisão de vocês: qual carteira cada pessoa deve ter, se o plano do cliente fica de pé, qual plano recomendamos e se a tese se sustenta diante de uma contestação.

**Entra:** perfil validado, diagnóstico e cardápio de carteiras (de `financeiro`). **Sai:** ou o plano recomendado com a tese estruturada (veredito, argumentos, premissas, riscos — cada argumento apontando para os números que o sustentam), ou um pedido de cálculo para `financeiro`.

**Loop com `financeiro`:** quando precisa de um número que não recebeu — avaliar um plano concreto no tempo, ou recalcular sob premissas contestadas (andar 5) — devolve um pedido de cálculo; o orquestrador leva a `financeiro` e traz a resposta. A ideia é pedir o mínimo: o cardápio de carteiras já chega calculado. O histórico de teses testadas e descartadas é guardado, porque vira argumento ("consideramos X e descartamos porque Y").

**Não vai aqui:** conta — todo número chega pronto; se faltar, é pedido, nunca calculado aqui. Nem a redação da apresentação (é `relatorio`).

**Fronteira com `validacao`:** `validacao` julga se o cliente se descreveu de forma coerente; `analista` julga se o plano é viável e é o melhor.

**Módulos internos** (ramos do fluxograma de decisão, não caixas separadas):
- `alocacao` — qual carteira para cada pessoa, escolhida no cardápio.
- `viabilidade` — o plano do cliente e o nosso ficam de pé?
- `defesa` — sustenta a tese sob contestação e só muda diante de evidência nova; o que conta como evidência nova é regra de vocês.

Metas e vontades declaradas como firmes pelo cliente (ex.: doar um valor a um filho) não são discutidas no mérito; o analista decide a forma. O que o cliente não decidiu (ex.: aceitar ou não uma proposta pela fazenda) é justamente o que o analista decide — não vira pergunta ao cliente.

**Decisões que são de vocês:** o fluxograma de decisão, critérios de alocação e de viabilidade, quando refutar o plano do cliente. Regras em `config/`, método em `docs/metodologia.md`.

**Natureza:** humana nas regras; o LLM só redige argumentos a partir dos números recebidos. **Estado:** vazio.
