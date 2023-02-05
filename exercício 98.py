from time import sleep


def contador(i, f, p):
    if f > i:
        li = list(range(i, f+1))
    else:
        li = list(range(f, i+1))
        li.sort(reverse=True)
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    print('-=' * 30)
    print(f'Contagem de {i} a {f} de {p} em {p}:')
    sleep(1)
    for c in li[::p]:
        print(f'{c}', end=' ')
        sleep(0.2)
    sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
print('-=' * 30 + '\nAgora faça você mesmo!!')
pri = int(input('Primeiro termo: '))
ult = int(input('Último termo: '))
pas = int(input('Pass: '))
contador(pri, ult, pas)

'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''