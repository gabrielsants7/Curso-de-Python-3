valor = float(input('Valor da casa: '))
salário = float(input('Salário do comprador: '))
tempo = int(input('Quantos anos de financiamento? '))
prestação = valor / (tempo * 12)
mínimo = salário * 30 / 100
if prestação <=mínimo:
    print(f'Para pagar um casa de R${valor:.2f} em {tempo} anos a prestação será de {prestação:.2f}')
    print('O empréstimo pode ser CONCEDIDO!')
else:
    print(f'Para pagar um casa de R${valor:.2f} em {tempo} anos a prestação será de {prestação:.2f}')
    print('Empréstimo NEGADO!') 
'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o 
empréstimo será negado.
'''