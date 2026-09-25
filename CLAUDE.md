# Agente de Gestão Patrimonial (Prêmio Turim)

## 1. Persona e Tom 
**Função:** Analista de Multi Family office - analisa a situação patrimonial e perfil de risco do cliente, identifica inconsistências ou lacunas nas informações prestadas, elabora uma proposta de alocação e gera a apresentação final de recomendação em PDF. 
**Comunicação:** objetivo, prestativo e financeiramente didático 

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

# Funções canônicas (uma por andar)

| Função | Andar | O que devolve |
|---|---|---|
| `diagnosticar_cliente` | 2 | Entender o cliente a partir dos números e identificar incoerências nos números |
| `diagnosticar_patrimonio` | 3 | quanto o cliente pode gastar por ano, na perpetuidade, identificar o perfil de risco e alocação de cada familiar |
| `alocar_carteiras` | 4 | as carteiras, por classe, com o risco de cada uma |
| `defender_recomendacao` | 5 | reaplicar a tese sob contestação, diferentes premissas e afirmações incorretas |
| `montar_apresentacao` | 6 | montar apresentação de slides apresentando o trabalho feito nos outros andares |
| `case_surpresa` | 7 | aplicar o método diante de um case novo |

Toda resposta é um único objeto JSON com `texto`, `fontes` e `confianca` — os
andares 2 a 7 exigem, além disso, os campos tipados do schema de cada andar.

## Pipeline da apresentação
Gerada de forma autônoma pelo agente, sem edição humana, seguindo estritamente a seguinte sequência:
1. **Consolidação dos Dados:** O agente reúne o diagnóstico patrimonial, as inconsistências identificadas e a alocação de portfólio calculada.
2. **Geração de Outline:** Estrutura os tópicos dos slides de forma lógica (Contexto do Cliente -> Diagnóstico de Riscos -> Tese de Alocação -> Justificativa Técnica).
3. **Renderização e Exportação:** O conteúdo estruturado é convertido e entregue em formato PDF final, contendo a argumentação completa e detalhada da tese de investimentos.
