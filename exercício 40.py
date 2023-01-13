nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))
média = (nota_1 + nota_2) / 2
print(f'Tirando {nota_1} e {nota_2}, a média do aluno é {média}')
if média > 7:
    print('O aluno está APROVADO.')
elif média < 5:
    print('O aluno está REPROVADO')
else:
    print('O aluno está em RECUPERÇÃO')

'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
com a média atingida:

Média abaixo de 5.0: REPROVADO

Média entre 5.0 e 6.9: RECUPERAÇÃO

Média 7.0 ou superior: APROVADO
'''