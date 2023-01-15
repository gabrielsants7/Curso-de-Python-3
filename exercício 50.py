soma = 0
cont = 0
for c in range(1,7):
    número = int(input('Digite o {} valor: '.format((c))))
    if número % 2 == 0:
        soma = soma + número
        cont = cont + 1
print('Você informou {}  números PARES  e a soma foi {}'.format(cont,soma))

'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
'''