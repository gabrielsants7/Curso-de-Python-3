km = float(input('Qual a velocidade do carro? '))
multa = float(km-80)*7
if km <=80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
        print(f'Você foi multato em R${multa:.2f} por exceder a velocidade máxima de 80km/h.')

'''
Escreva um programa que leia a velocidadew de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar R$7,00  por cada km acima do limite.
'''