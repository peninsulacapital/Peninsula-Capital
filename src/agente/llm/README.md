# llm
**Papel:** único ponto de contato com o modelo de linguagem. Isola qual provedor/modelo usamos atrás de uma interface simples.

**Entra:** um prompt e o formato de resposta esperado. **Sai:** texto ou objeto estruturado.

**Não vai aqui:** o conteúdo dos prompts (fica em `prompts/`), nem decisão de negócio.

**Por que existe:** trocar de LLM não pode exigir mexer em nenhuma outra pasta.

**Natureza:** robótica. **Estado:** vazio — modelo ainda não escolhido.
