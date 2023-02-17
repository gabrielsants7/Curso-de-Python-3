def voto(ano=0):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return idade, 'NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return idade, 'VOTO OPICIONAL'
    else:
        return idade, 'VOTO OBRIGATÓRIO'


# Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(f'Com {voto(nasc)[0]} anos: {voto(nasc)[1]}')

'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de 
uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO 
nas eleições.
'''