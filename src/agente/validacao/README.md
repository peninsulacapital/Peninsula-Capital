# validacao
**Papel:** o juízo crítico do agente. Recebe o que `interpretacao` traduziu "cegamente" do texto do cliente e verifica se fecha: detecta incoerência entre informações e ausência de dado julgado necessário para a análise.

**Entra:** o perfil de `interpretacao`. **Sai:** ou o perfil aprovado, ou uma pergunta de esclarecimento para o cliente.

**Funciona em loop:** ao achar incoerência ou lacuna bloqueante, gera uma pergunta de esclarecimento em vez de seguir adiante. A resposta volta para `interpretacao` e o ciclo se repete até o perfil fechar. **Nunca assume no lugar do cliente** — isso é o diferencial que a banca avalia; assumir e seguir em frente é o erro a evitar.

**Não vai aqui:** montar carteira, projetar patrimônio, decidir a pergunta em linguagem natural (isso é redigido via `llm`/`prompts` a partir do motivo estruturado que `validacao` aponta).

**Decisões que são de vocês:** o que conta como incoerência, o que é lacuna bloqueante versus contornável, o texto/critério de cada checagem. As regras ficam parametrizadas em `config/`.

**Natureza:** humana — é onde está o diferencial do projeto. **Estado:** vazio.

## Perfil de risco
`interpretacao` só registra as declarações do cliente sobre risco (perda tolerada, experiência, reação a quedas, preferências). Consolidá-las num perfil é daqui: exige decidir qual declaração prevalece quando elas se contradizem, e só `validacao` pode perguntar ao cliente. As categorias e os critérios do perfil são de vocês — ainda a estruturar.

## Exemplos de checagem (a parametrizar em `config/`)
- Declarações de risco contraditórias (ex.: patrimônio concentrado em ativo de alto risco e tolerância zero a perda).
- Números que não fecham (ex.: total declarado pelo cliente vs. soma dos itens).
- Falta de dado essencial para a análise.
