# Caixa `analista` absorve `portfolio`, em loop com `financeiro`

**Decidido:** o pipeline passa a ser `interpretacao` ⇄ `validacao` → `financeiro` ⇄ `analista` → `relatorio`. `financeiro` só faz contas; `analista` concentra todo o juízo — alocação, viabilidade, defesa — organizado em módulos internos. `relatorio` só apresenta. A caixa `portfolio` deixa de existir.

**Alternativas consideradas:**
- Juízo espalhado (carteira em `portfolio`, viabilidade em `financeiro`, linha argumentativa em `relatorio`). Descartada: ninguém era dono do veredito nem da defesa sob contestação (andar 5).
- `portfolio` e `analista` separados, em esteira linear. Descartada: o analista só julgaria cenários já calculados e não conseguiria recalcular sob premissas contestadas.
- Loop de três caixas: `analista` propõe tese → `portfolio` → `financeiro` → `analista`. Descartada: com duas classes em duas regiões (regras da banca), a carteira é a escolha de poucos pesos. O cálculo de risco e retorno é conta (`financeiro`) e a escolha é decisão (`analista`); `portfolio` viraria só um repassador.

**Por quê:** separa calcular de decidir e de apresentar, com um dono para cada juízo. Para manter os pedidos ao `financeiro` no mínimo, a primeira passada já entrega o cardápio completo de carteiras (a fronteira eficiente); o analista só volta para avaliar um plano concreto no tempo ou recalcular sob contestação.

**Quando rever:** se a construção de carteira passar a exigir método pesado próprio (muitas classes, otimizador com restrições), ele entra como motor de cálculo ao lado de `financeiro`, não como caixa entre ele e o `analista`.
