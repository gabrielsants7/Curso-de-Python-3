import math
a = float(input('Dgite o ângulo que você deseja:'))
se = math.sin (math.radians(a))
co = math.cos(math.radians(a))
ta = math.tan(math.radians(a))
print(f'O ângulo de {a} tem o SENO de {se:.2f}')
print(f'O ângulo de {a} tem o COSSENO de {co:.2f}')
print(f'O ângulo de {a} tem a TANGENTE de {ta:.2f}')

'''
Faça um program que  leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
'''