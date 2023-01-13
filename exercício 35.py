print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
primeiro = float(input('Primeiro segmento: '))
segundo = float(input('Segundo segmento: '))
terceiro = float(input('Terceiro segmento: '))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')

'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se  elas podem ou não formar um 
triângulo.
'''