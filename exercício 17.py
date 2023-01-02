from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = hypot(co,ca)
print(f'O valor da hipotenusa é {hi:.2f}')

'''
Faça um programa que leia o comprimento do  cateto oposto e cateto adjacente de um triângulo  retângulo, 
calcule e mostre o comprimento da hipotenusa
'''