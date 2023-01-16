end = 0
soma = 0
cont = 0
c = 999
while end != 999:
    número = int(input('Digite um número [999 para parar]: '))
    soma += número
    cont += 1
    if número == 999:
        end = 999
        soma -= 999
        cont -= 1
print('fim')
print('você digitou {} números a soma entre eles foi {}'.format(cont,soma))

'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag).
'''