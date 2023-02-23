import moedas

preço = float(input('Digite o preço: R$ '))
print(f'\nA metade do preço é R$ {moedas.metade(preço):.1f}')
print(f'O dobro vale R$ {moedas.dobro(preço):.1f}')
print(f'Aumentando 10 % do preço, temos R$ {moedas.aumentar(preço):.1f}')

'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''