"""Único lugar que conhece a ordem das etapas do pipeline.

interpretacao <-> validacao -> financeiro <-> analista -> relatorio

interpretacao e validacao rodam em loop: enquanto validacao apontar
incoerencia ou lacuna bloqueante, gera uma pergunta ao cliente, a resposta
volta para interpretacao, e o ciclo se repete ate o perfil fechar.

financeiro e analista rodam em loop: financeiro entrega diagnostico e
cardapio de carteiras; se o analista precisar de outro numero, devolve um
pedido de calculo, que volta para financeiro, ate o analista fechar o plano.

mercado e schemas nao aparecem na cadeia: sao consultados pelas caixas que
precisam deles, nao ocupam uma posicao fixa.

Vazio por enquanto: cada etapa e ligada aqui quando sua caixa existir.
"""
