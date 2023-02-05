print('nome do jogador'.upper())
dados = dict()
partidas = list()
dados['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, total):
    partidas.append(int(input(f'Quantos gols na {c + 1}º partida? ')))
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)
print(dados)
print('**' * 18)
for k, v in dados.items():
    print(f'o campo {k} tem o valor {v}')
print('**' * 18)
print(f'O jogador {dados["nome"]} jogou {total} partidas')
for r, n in enumerate(partidas):
    print(f'Na {r+1}º partida, {dados["nome"]} fez {n} gols')
print(f'totalizando {dados["total"]} gols')

'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador 
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso 
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''