pessoas = []
while True:
    nome = input('Nome: ')
    peso = float(input('Informe o peso em KG: '))
    pessoas.append([nome,peso])
    continua = input('Quer continuar? [S/N] ')
    if continua in 'nN':
        break
peso_descrescente = sorted(pessoas, key=lambda p: p[1], reverse=True)
maior_peso, menor_peso = peso_descrescente[0][1], peso_descrescente[-1][1]
lista_maior_p = [pessoa[0] for pessoa in pessoas if pessoa[1] == maior_peso]
lista_menor_p = [pessoa[0] for pessoa in pessoas if pessoa[1] == menor_peso]
print('-='*25)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior_peso} kg. Peso de {lista_maior_p}')
print(f'O menor peso foi de {menor_peso} kg. Peso de {lista_menor_p}')

'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves
'''