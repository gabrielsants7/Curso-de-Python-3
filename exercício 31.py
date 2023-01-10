distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar um viagem de {:.1f}km'.format(distância))
if distância <=200:
    print(f'E o preço da sua passagem será de R${distância * 0.50:.2f}')
else:
    print(f'E o preço da sua passagem será de R${distância * 0.45:.2f}')

'''
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando
R$0,50 para de viagens de até 200km e R$0,45 para viagens mais  longas
'''