import moedas


p = int(input('Digite o preço: R$'))
print(f'A metade de R${p},00 é R${int(moedas.metade(p))},00')
print(f'O dobro de R${p},00 é R${moedas.dobro(p)},00')
print(f'Aumentando 10%, temos R${int(moedas.aumentar(p, 10))},00')

'''
Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números 
como um valor monetário formatado.    
'''