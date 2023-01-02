from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação será: {lista} ')

'''
O mesmo professor do desafio anterior  quer sortear a ordem de apresentação de trabalho dos alunos.Faça 
um programa que leia  o nome dos quatros alunos e mostre em ordem sorteada
'''