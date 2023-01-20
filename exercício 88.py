from time import sleep
from random import randint
jogadas = []
jogada = []
print('-' *45)
print('             JOGOS NA MEGA SENA')
print('-' *45)
p = int(input('Quantos jogos você quer que eu sorteie: '))
print()
print('-=' * 6, f'SORTEANDO {p} JOGO(S)', '-=' * 6)
print()
for jogos in range(1, p+1):
    while len(jogada) != 6:
        n = randint(1, 60)
        if n not in jogada:
            jogada.append(n)
    jogadas.append(sorted(jogada[:]))
    jogada.clear()
for i, v in enumerate(sorted(jogadas)):
    print(f'Jogo {i+1}: {v}')
    sleep(1)
print()
print('-=-=-=-=-= > BOA SORTE! < -=-=-=-=-=')

'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos 
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''