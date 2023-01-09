import random 
números = [0,1,2,3,4,5]
numbers = random.choice(números)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
adivinhação = int(input('Em que número eu pensei? '))
print('processando...')
if adivinhação == (numbers):
    print('PARABÉNS!Você conseguiu me vencer!')
else:
    print(f'GANHEI!Eu pensei no número {numbers} e não no {adivinhação}!')

'''
Escreva um programa que faça o computador "pensar" em um número inteiro de 0 a 5 e peça para o usuário tentar 
descobrir qual foi o número escolhido pelo computador. O programa deverá  escrever na tela se o usuário venceu
ou perdeu
'''