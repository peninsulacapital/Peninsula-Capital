# financeiro
**Papel:** o fazedor de contas. Funções determinísticas, sem LLM e sem decisão: recebe perfil, premissas de mercado e, quando houver, um plano, e devolve números.

**Dois modos:**
- **Diagnóstico** (sem plano, primeira passada): variáveis derivadas do perfil (patrimônio total e investível, imposto de uma venda, gasto real por moeda, conversões de periodicidade e de valores relativos) e o **cardápio de carteiras** — risco e retorno de cada combinação de pesos numa grade (a fronteira eficiente). O cardápio depende só de `mercado`, não do cliente.
- **Avaliação** (a pedido do `analista`): o que acontece com um plano concreto ao longo do tempo — venda, doações, carteiras, gastos, com imposto e inflação — inclusive sob premissas alteradas.

**Entra:** perfil validado, premissas de `mercado` e, na avaliação, o pedido do `analista`. **Sai:** números — nunca um veredito.

**Não vai aqui:** escolher carteira ou plano, julgar viabilidade (isso é `analista`), nem escrever texto.

**Natureza:** robótica na implementação, humana na metodologia. Nenhuma fórmula entra sem vocês definirem. **Estado:** vazio.
