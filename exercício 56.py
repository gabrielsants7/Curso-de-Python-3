soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('------ {}ª PESSOA ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade >  maior_idade_homem:
        maior_idade_homem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

media_idade = soma_idade / 4
print('A média de idade do grupo é {}'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem,nomevelho))
print('Ao todo são {] mulheres  com menos de 20 anos'.format(totmulher20))

'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''