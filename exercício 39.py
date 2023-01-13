from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
     saldo_1 = 18 - idade
     print(f'Ainda falta {saldo_1} anos para o seu alistamento')
     ano_2 = atual + saldo_1
     print(f'Seu alistamento será em {ano_2}')
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado a {saldo}')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')

'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai
se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''