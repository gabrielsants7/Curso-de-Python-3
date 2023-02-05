jogador={}
lista=[]
gols=[]
while True:
    soma=0
    jogador['nome']=input("Digite o nome do jogador: ")
    part=int(input(f'quantas partidas {jogador["nome"]} jogou? '))
    for cont in range(0, part):
        a=int(input(f'Digite quantos gols foram feitos no {cont+1}º jogo: '))
        soma+=a
        gols.append(a)
    jogador['gols']=gols[:]
    jogador['total']=soma
    lista.append(jogador.copy())
    gols.clear()
    cond=input('Deseja continuar? [S/N]: ').upper()[0]
    if cond =='N':
        break
print('\033[33m='*60)
print('{:^60}'.format('TABELA'))
print('\033[33m='*60, '\033[m')
print('cod\tnome\t\tgols\t\ttotal')
print('-'*60)
for v, k in enumerate (lista):
    print(f'{v:<8}', end='')
    for cont in k.values():
        print('{:<16}'.format(str(cont)), end='')
    print('')
print('Mostrar dados de qual jogador? 999 para parar')
while True:
    num=int(input('Digite o código do jogador: '))
    if num == 999:
        break
    print(f'LEVANTAMENTO do jogador {lista[num]["nome"]}:')
    for v, k in enumerate (lista[num]['gols']):
        print(f'No jogo {v+1} fez {k} gols')
    print('-'*60)
print('\033[31m-'*60)
print('{:^60}'. format('PROGRAMA ENCERRADO'))
print('-'*60)

'''
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes 
do aproveitamento de cada jogador.
'''