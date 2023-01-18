número = ((int(input('insira um número: '))),
       (int(input('Insira outro número: '))),
       (int(input('Insira mais um número: '))),
       (int(input('Insira o último número: '))))
print(f'O valor 9 apareceu {número.count(9)} vezes na tupla.')
if 3 in número:
    print(f'O valor 3 apareceu pela primeira vez na {número.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares  digitados foram ', end='')
for n in número:
    if n % 2 == 0:
        print(n, end='')

'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''