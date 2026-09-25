# prompts
**Papel:** os textos de instrução enviados ao LLM, um arquivo por tarefa, versionados como código.

**Usado por:** `interpretacao` (extrair dados do texto do cliente), `validacao` (redigir a pergunta de esclarecimento), `analista` (redigir os argumentos da tese e a resposta a contestações) e `relatorio` (redigir a apresentação).

**Não vai aqui:** código Python, valores numéricos.

**Por que separado:** é o que vocês mais vão reescrever e comparar. Ficando em arquivos próprios, dá para editar e versionar sem tocar em lógica.

**Natureza:** assistida — Claude propõe, vocês refinam. **Estado:** vazio.
