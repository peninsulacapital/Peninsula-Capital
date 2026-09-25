# Estrutura inicial do perfil do cliente (`ClientProfile`)

Estrutura inicial, feita para mudar sob demanda quando as contas pedirem. As definições de cada campo moram no próprio schema; aqui fica só o porquê.

**Cada dado é uma declaração** (`Declared`): status (`stated`, `approximate`, `ambiguous`, `absent`) + valor + trecho literal do texto.
- O status é o gatilho da `validacao`.
- O trecho é a trava mecânica contra dado inventado ("quem inventa dados toma decisão sobre uma empresa que não existe"): o Python confere se ele existe no texto do cliente. Também permite à validação citar o cliente na pergunta.

**O LLM transcreve, não calcula.** Pode mudar a notação (R$ 300MM → 300000000), mas nunca combinar dois números: periodicidade e valores relativos ("4% dos R$ 25MM") ficam como ditos e `financeiro` converte.
- Alternativa: permitir conversões diretas. Descartada por ora — o número convertido não aparece no trecho, o que quebra a conferência, e "nunca faça conta" é uma regra mais robusta para o LLM do que "só contas fáceis". Rever se gerar trabalho demais.

**Tudo opcional no schema.** Um campo obrigatório quebraria a interpretação justamente quando falta dado. O que é obrigatório para a análise mora em `config/` e é aplicado pela `validacao`.

**Generalidade:** ativos e passivos têm descrição livre + categoria curta + atributos econômicos. Todo fluxo recorrente (renda de ativo, custo, parcela de dívida) mora em `flows`, ligado por id ao ativo ou passivo — um dono por informação.

**Vontades do cliente com firmeza de dois níveis** (`firm` / `open`), em vez de três. O que importa ao `analista` é se o assunto está em discussão: o que é firme não se discute no mérito, só na forma. Menos classes, menos ambiguidade para o LLM.

**Blocos que não são fatos:** crenças do cliente (a verificar pelo analista), preferências e restrições, declarações de risco (a classificar pela validação), agregados (a conferir contra a soma dos itens).

**Negativas declaradas** ("não temos dívidas") separadas de ausência: sem elas, a validação perguntaria o que o cliente já respondeu.
