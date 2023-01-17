end = 0
soma = 0
cont = 0
c = 999
while True:
    número = int(input('Digite um número [999 para parar]: '))
    soma += número
    cont += 1
    if número == 999:
        end = 999
        soma -= 999
        cont -= 1
        break
print('fim')
print(f'Você digitou {cont} números a soma entre eles foi {soma}')

'''
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''