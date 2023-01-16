print("GERADOR DE PA")
print(f'{"-="*10}')
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
passo = 1
total = 0
mais = 10
while mais != 0:
    total =  total + mais
    while passo <= 10:
        print(termo, end=' → ' if passo < 10 else '')
        passo += 1
        termo += razao
    print(' PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada ocm {} termos mostrados'.format(total))
print('FIM')

'''
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
 elementos de uma Sequência de Fibonacci. 

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
'''
