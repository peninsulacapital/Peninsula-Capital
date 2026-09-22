"""Único lugar que conhece a ordem das etapas do pipeline.

interpretacao -> validacao -> financeiro -> portfolio -> relatorio

interpretacao e validacao rodam em loop entre si: enquanto validacao apontar
incoerencia ou lacuna bloqueante, gera uma pergunta ao cliente, a resposta
volta para interpretacao, e o ciclo se repete ate o perfil fechar.

mercado e schemas nao aparecem na cadeia: sao consultados pelas caixas que
precisam deles, nao ocupam uma posicao fixa.

Vazio por enquanto: cada etapa e ligada aqui quando sua caixa existir.
"""
