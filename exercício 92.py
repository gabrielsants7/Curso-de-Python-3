from datetime import datetime
dados={}
while True:
    dados['Nome']=input('Nome: ').strip().title()
    nas= int(input('Ano de nascimento: '))
    dados['idade']= datetime.now().year - nas
    dados['ctps']=int(input('Carteira de trabalho (0 não tem): '))
    if dados['ctps'] == 0:
        break
    dados['Contratação']=int(input('Ano de contratação: '))
    dados['Salario']=int(input('Salario: R$ '))
    dados['Aposentadoria']= dados['idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
    break

print('='*35)
for a, b in dados.items():
    print(f'-- {a}: {b}')

'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um 
dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação 
e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''