número = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{número} convertido para binário é igual a {bin(número)}')
elif opção == 2:
    print(f'{número} convertido para OCTAL é igual a {oct(número)}')
elif opção == 3:
    print(f'{número} convertido para HEXADECIMAL é igual a {hex(número)}')
else:
    print('Opçãoinválida. Tente novamente.')

'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''