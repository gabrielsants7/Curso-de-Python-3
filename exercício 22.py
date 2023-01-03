n = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
espaço = n.strip()
maiúsculo = n.upper()
minúsculo = n.lower()
letras = len(n) - n.count(' ')
primeiro = n.find(' ')

print(f'Seu nome em letras maiúsculas: {maiúsculo}!')

print(f'Seu nome em letras minúsculas: {minúsculo}!')

print(f'Seu nome tem {letras} letras!')

print(f'Seu primeiro nome tem {primeiro} letras!')

'''
Crie um programa que leia o nome completo de uma pessoa e mostre
O nome com todas as letras maiúsculas e minúsculas 
Quantas letras ao todo(sem considerar espaços)
Quantas letras tem o primeiro nome
'''