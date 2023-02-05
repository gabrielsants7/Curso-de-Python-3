pessoa = dict()
lista = list()
while True:
    pessoa['Nome'] = str(input('Nome: ')).strip().title()
    pessoa['Media'] = float(input(f'Media de {pessoa["Nome"]}: '))
    operador = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if pessoa['Media'] >= 7:
        pessoa['Situação'] = 'APROVADO'
    elif 5 < pessoa['Media'] < 7:
        pessoa['Situação'] = 'RECUPERAÇÂO'
    else:
        pessoa['Situação'] = 'REPROVADO'
    lista.append(pessoa.copy())
    if operador not in "SN":
        operador = str(input('Escreva apenas [S/N]: ')).upper().strip()[0]
    if operador in "N":
        break
for p in lista:
    print('-' * 19)
    for n, k in p.items():
        print(f'{n}: {k}')
print('-' * 19)

'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, 
mostre o conteúdo da estrutura na tela.
'''