from random import randint
V = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador  + computador
    tipo = ' '
    while tipo not in  'PI':
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador}  e o computador {computador}. Total de {total}',END='')
    print('DEU PAR' if total %2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total %2 == 0:
            print('VOCÊ VENCEU!')
            V += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total %2 == 0:
            print('VOCÊ VENCEU!')
            V += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {V} vezes.') 

'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''