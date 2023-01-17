print('-'*40)
print('          LOJA SUPER BARATÃO')
print('-'*40)
total = totmil = menor = cont = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos com o valor acima de R$1000.00')
print(f'O produto mais barato foi {barato}  que custa {menor:.2f}')

'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o 
usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
'''