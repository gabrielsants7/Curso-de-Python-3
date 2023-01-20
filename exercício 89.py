dados = []
nomes = []
nota = []
notas = []
media = 0
médias = []
alunos_cadastrados = 0
import math
while True:
    nomes.append(str(input('Nome do aluno: ')))
    nota1 = float(input('1 NOTA: '))
    nota2 = float(input('2 NOTA: '))

    nota.append(nota1)
    nota.append(nota2)

    media = (nota1 + nota2)/2
    médias.append(media)
    notas.append(nota[:])
    nota.clear()

    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if continuar in 'SN':
            break
        else:
            print('\033[;31mOpção Inválida!\033[m')
    if continuar == 'N':
        break

    alunos_cadastrados += 1

dados.append(nomes[:])
dados.append(notas[:])
dados.append(médias[:])
print('-='*35)
print('N°   NOME                MÉDIA')
print('-'*50)


for c1 in range(0, len(dados[0])):
    print(f'{c1:^2}   {dados[0][c1]:<20} {dados[2][c1]:^4}')
print('-'*50)
from time import sleep
while True:
    pergunta = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if pergunta == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        sleep(2)
        break
    else:
        print(f'As notas de {dados[0][pergunta]} são: {dados[1][pergunta]}')
        print('-' * 50)

'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a 
média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''