# schemas
**Papel:** o contrato de dados do projeto. Define, em Pydantic, as estruturas que trafegam entre as caixas — o perfil do cliente, as premissas de mercado, o plano, o resultado.

**Entra:** nada (é definição). **Sai:** tipos usados por todo mundo.

**Não vai aqui:** cálculo, leitura de arquivo, regra de negócio. Só a forma do dado (inclui checar que ids referenciados existem).

**Por que é transversal:** é o que permite trocar a implementação de uma caixa sem quebrar as outras. Mudança aqui afeta todos, então muda devagar e com acordo dos dois.

**Arquivos:**
- `base.py` — `Declared` (todo dado do cliente: status + valor + trecho literal), quantias (`Money`, `Share`).
- `client_profile.py` — `ClientProfile`, a saída de `interpretacao`: pessoas, ativos, passivos, fluxos, eventos, objetivos, crenças, preferências, declarações de risco, agregados, negativas e o que não coube.

As **descrições dos campos são as definições** que o LLM do interpretador recebe: mudar um conceito é mudar a descrição aqui. Identificadores em inglês, descrições em português. O porquê das escolhas: `docs/decisoes/2026-09-25-perfil-do-cliente.md`.

**Tudo é opcional no schema.** O que é obrigatório para a análise não mora aqui: fica em `config/` e é aplicado por `validacao`.

**Natureza:** vocês definem os campos, Claude implementa. **Estado:** perfil do cliente pronto como estrutura inicial — muda sob demanda quando as contas pedirem. Premissas de mercado, plano e resultado ainda vazios.
