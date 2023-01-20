lista = []
while True:
    lista.append(int(input('Digite um valor: '))) 
    lista.sort(reverse=True)
    pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()
    var = pergunta == 'SN'
    if pergunta == 'S':
        continue
    if pergunta == 'N':
        break
    while pergunta not in 'SN':
        pergunta = str(input('Escreva apenas [S] para SIM e [N] para Não : ')).upper().strip()
    if pergunta == 'S':
        continue
    if pergunta == 'N':
        break
print('=-'*40)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem descrescente são {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 NÃO está na lista.')

'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''