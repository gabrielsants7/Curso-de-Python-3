def calc_area():
    print(' CONTROLE DE TERRENOS ')
    print('-'*27)
    larg = float(input('Digite a largura (m): '))
    comp = float(input('Digite o cumprimento (m): '))
    total = larg*comp
    print(f'A área de um terreno {larg:.1f}x{comp} é de {total}m²')


calc_area()

'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular 
(largura e comprimento) e mostre a área do terreno.
'''