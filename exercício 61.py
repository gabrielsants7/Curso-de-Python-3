print("GERADOR DE PA")
print(f'{"-="*10}')
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
passo = 1
while passo <= 10:
    print(termo, end=' → ' if passo < 10 else '')
    passo += 1
    termo += razao
print(' FIM')

'''
Refaça o exercício 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''