# Agente de Gestão Patrimonial — Prêmio Turim

Agente em Python que recebe a descrição de um cliente em texto livre, critica o que está incoerente ou faltando, monta um plano de gestão patrimonial com teoria de portfólio e entrega uma apresentação em PDF explicando a tese.

## Por onde começar
- **Convenções e forma de trabalho:** [CLAUDE.md](CLAUDE.md)
- **Regras do desafio:** [docs/regras_banca.md](docs/regras_banca.md)
- **Mapa do código:** [src/agente/README.md](src/agente/README.md)

Cada pasta tem um `README.md` dizendo o que é dela, o que não é, e quem preenche.

## Estado
Esqueleto montado, todas as caixas vazias. Construção bottom-up: do fornecimento de dados em direção ao relatório, uma caixa por vez.

## Ambiente
```
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\python -m pytest
```
