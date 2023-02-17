def ficha(nome='desconhecido', gol=0):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if not gol.isnumeric():
        gol = '0'
    return f'O jogador {nome} fez {gol} gols no campeonato'

# programa principal
jogador = str(input('Nome do jogador: '))
gol = str(input('Número de gols: '))
print(ficha(jogador, gol))

'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador 
e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado 
não tenha sido informado corretamente.
'''