# Agente de Gestão Patrimonial (Prêmio Turim)

Agente de IA em Python: recebe texto livre com a situação patrimonial, objetivos e perfil de risco do cliente; identifica incoerências e informações faltantes; monta um plano e uma carteira com teoria de portfólio; entrega uma apresentação em PDF explicando a tese.

Trabalham no projeto duas pessoas mais o Claude. Este arquivo é a fonte de verdade das convenções e da forma de trabalho.

## Como trabalhar (vale para toda sessão)

1. **Propor antes de implementar.** Nesta fase, descrever o que pretende fazer e esperar o "pode ir". Vale inclusive para o que parece óbvio ou pequeno. Nada de entregar código não solicitado junto com a resposta.
2. **Uma caixa por vez, bottom-up.** A ordem é do fornecimento de dados em direção ao relatório. Não adiantar etapas seguintes nem criar "só o esqueleto" de uma caixa futura.
3. **Metodologia é dos especialistas.** Cálculo de risco, inflação, retorno, otimização, conversão de moeda: o método é definido pelos humanos e registrado em `docs/metodologia.md` antes de virar código. Na dúvida sobre como calcular, perguntar — nunca escolher uma abordagem por conta própria, nem "por enquanto".
4. **Não produzir números fora de tarefa.** Rodar estatística sobre os dados só quando pedido, e o resultado vai para onde foi combinado, não para dentro da documentação.
5. **Sem redundância.** Cada informação tem **um único dono**, declarado no `README.md` da pasta. Outros arquivos referenciam por link; não repetem o conteúdo. Antes de escrever um número ou uma regra, verificar se ela já tem dono.

## Princípios do produto

- **LLM interpreta e redige; Python calcula.** O LLM não produz número final. Exceções são registradas em `docs/decisoes/`.
- **Nunca inventar dado do cliente.** O que não foi dito fica marcado como ausente e passa por `validacao`, que pergunta ou assume de forma explícita — e a suposição aparece no relatório.
- **Regra de especialista mora em `config/` (YAML)**, não enterrada no código.
- **Trocar de LLM não pode exigir mexer fora de `src/agente/llm`.**
- **`data/raw/` é somente leitura.**

## Convenções

- Pastas e documentos em **português**, com nomes diretos. Identificadores de código em **inglês**. Texto ao usuário e relatório em português.
- Dados entre caixas trafegam como objetos de `src/agente/schemas`, nunca dicionários soltos.
- Cada pasta tem `README.md` no mesmo formato: papel, o que entra e sai, o que **não** vai ali, natureza e estado. Mexeu na pasta, atualiza o README.
- Decisão relevante vira nota em `docs/decisoes/AAAA-MM-DD-titulo.md`.
- Cálculo financeiro só entra com teste de valor conferido à mão.

## Mapa

Pipeline: `interpretacao` ⇄ `validacao` (loop de esclarecimento) → `financeiro` → `portfolio` → `relatorio`.
Transversais: `schemas`, `mercado`, `llm`, `prompts`. Ordem das etapas só em `orquestrador.py`.
Detalhe de cada caixa no seu próprio README; mapa geral em `src/agente/README.md`.

## Onde cada um foca

- **Especialistas:** `validacao`, `portfolio`, `config`, `docs/metodologia.md`, `inputs/casos`.
- **Claude:** `mercado`, `financeiro` (implementação da metodologia dada), `llm`, geração do PDF, testes.

## Ambiente

Python 3.11+ (3.14 em uso). `python -m venv .venv`, `.venv\Scripts\pip install -r requirements.txt`, testes com `.venv\Scripts\python -m pytest`. `pyproject.toml` já aponta `src/` para o pytest. Dependência nova entra quando a caixa que precisa dela for construída.

## Estado

Esqueleto de pastas montado, **todas as caixas vazias**. Regras da banca transcritas em `docs/regras_banca.md`; planilha histórica recebida em `data/raw/`, ainda não lida por código.

Próximo passo combinado: nenhum até definição conjunta.
