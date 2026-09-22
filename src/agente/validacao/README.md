# validacao
**Papel:** o juízo crítico do agente. Recebe o que `interpretacao` traduziu "cegamente" do texto do cliente e verifica se fecha: detecta incoerência entre informações e ausência de dado julgado necessário para a análise.

**Entra:** o perfil de `interpretacao`. **Sai:** ou o perfil aprovado, ou uma pergunta de esclarecimento para o cliente.

**Funciona em loop:** ao achar incoerência ou lacuna bloqueante, gera uma pergunta de esclarecimento em vez de seguir adiante. A resposta volta para `interpretacao` e o ciclo se repete até o perfil fechar. **Nunca assume no lugar do cliente** — isso é o diferencial que a banca avalia; assumir e seguir em frente é o erro a evitar.

**Não vai aqui:** montar carteira, projetar patrimônio, decidir a pergunta em linguagem natural (isso é redigido via `llm`/`prompts` a partir do motivo estruturado que `validacao` aponta).

**Decisões que são de vocês:** o que conta como incoerência, o que é lacuna bloqueante versus contornável, o texto/critério de cada checagem. As regras ficam parametrizadas em `config/`.

**Natureza:** humana — é onde está o diferencial do projeto. **Estado:** vazio.
