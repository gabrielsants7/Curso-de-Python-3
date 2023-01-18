times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Internacional', 'Fluminense', 'Corinthians', 'Athletico-PR', 
'Atlético', 'Fortaleza', 'São Paulo', 'América', 'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino', 
'Coritiba', 'Cuiabá', 'Grêmio', 'Vasco', 'Bahia')
print('-='*15) 
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os cinco primeiros são {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'O Fortaleza está na {times.index("Fortaleza")+1}ª posição')

'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.
'''