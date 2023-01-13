peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura * altura)
print(f'O IMC dessa pessoa é {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO NORMAL')
elif imc < 25:
    print('Parabéns, você está na faixa de PESO IDEAL')
elif imc < 30:
    print('Você está SOBREPESO')
elif imc < 40:
    print('Você está em OBESIDADE')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
 
'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
mostre seu status, de acordo com a tabela abaixo:

IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida
'''