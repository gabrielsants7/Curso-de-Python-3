nome = str(input('Digite seu nome: ')).strip()
print('Prazer em te conhecer!')
m = nome.split()
print(f'Seu primeiro nome é {m[0]}')
print('Seu ultimo nome é {}'.format(m[len(m)-1]))

'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome 
separadamente
'''