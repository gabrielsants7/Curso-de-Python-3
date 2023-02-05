from time import sleep

def bigger(x):
    print('-='*30)
    for v in x:
        print(f'{v} ', end='')
        sleep(0.5)
    print(f'Foram informados {len(x)} valores ao todo.')
    if len(x) > 0:
        print(f'O maior valor é {max(x)}.')
    else:
        print('O maior valor é 0.')
    sleep(1)

bigger([2, 9, 4, 5, 7, 1])
bigger([4, 7, 0])
bigger([1, 2])
bigger([6])
bigger([])

'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''