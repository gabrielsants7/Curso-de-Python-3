soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador = contador + 1     
        soma = soma + c
print(f'A soma de todos os {contador} valores solicitados é {soma}')

'''
Faça um programa que calcule a soma entre todos os números que são múltiplos de três
e que se encontram no intervalo de 1 até 500.
'''