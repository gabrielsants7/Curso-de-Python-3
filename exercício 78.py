valores = []

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print(f'Os números digitados foram: {valores}')
print(f'O Maior valor foi {max(valores)} na(s) posição(ões):', end = ' ')

for c in range(0, 5):
    if valores[c] == max(valores):
        print(f'{c + 1} ', end = ' ')
        
print(f'\nO Menor valor foi {min(valores)} na(s) posição(ões):', end = ' ')

for c in range(0, 5):
    if valores[c] == min(valores):
        print(f'{c + 1} ', end = ' ')

'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e 
o menor valor digitado e as suas respectivas posições na lista. 
'''