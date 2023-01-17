while True:
    print('='*35)
    número = int(input('Quer ver a tabuada de qual valor? '))
    print('='*35)
    for c in range(1,11):
        print(f'{número} x {c:2} = {número*c}')
    print('='*35)
    if número < 0:
        break
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')

'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo. 
'''