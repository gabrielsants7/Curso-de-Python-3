salário = float(input('Qual é o salário do funcionário? R$'))
if salário >= 1.250:
    aumento_10 = (salário * 1.10)
    print(f'Quem ganhava R${salário:.2f} passa a ganhar {aumento_10:.2f} agora')
else:
    aumento_15 = (salário * 1.15)
    print(f'Quem ganhava {salário:.2f} passa a ganhar {aumento_15:.2f} agora')

'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores  a R$1.250,00, calcule um aumento de 10%.Para os inferiores ou iguais, o aumento 
é de 15%.
'''