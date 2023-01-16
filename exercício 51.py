print(f'{"="*40}')
print("         10 TERMOS DE UMA PA")
print(f'{"="*40}')
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for c in range(1, 11):
    print(termo, end=' → ' if c < 10 else '')
    termo += razao
print(' ACABOU')

'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 
10 primeiros termos dessa progressão.
'''