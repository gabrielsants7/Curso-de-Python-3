import coins


preço = float(input('Preço: R$'))
m = coins.moeda(preço)
met = coins.metade(preço)
d = coins.dobro(preço)
aum = coins.aumento(preço)
print('A metade de {} é {}'.format(m, met))
print('O dobro de {} é {}'.format(m, d))
print('Aumentando 10% temos {}'.format(aum))

'''
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se 
o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''