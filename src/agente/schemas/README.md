# schemas
**Papel:** o contrato de dados do projeto. Define, em Pydantic, as estruturas que trafegam entre as caixas — o perfil do cliente, as premissas de mercado, o plano, o resultado.

**Entra:** nada (é definição). **Sai:** tipos usados por todo mundo.

**Não vai aqui:** cálculo, leitura de arquivo, regra de negócio. Só a forma do dado.

**Por que é transversal:** é o que permite trocar a implementação de uma caixa sem quebrar as outras. Mudança aqui afeta todos, então muda devagar e com acordo dos dois.

**Natureza:** vocês definem os campos, Claude implementa. **Estado:** vazio.
