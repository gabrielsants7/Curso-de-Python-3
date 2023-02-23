def leiaint(n):
    print('-'*24)
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except:
            n = print('\033[0;31mVocê digitou uma opção inválida, tente de novo.\033[m')
        else:
            break
    return n
def leiaFloat(n):
    print('-'*24)
    while True:
        try:
            n=float(input('Digite um número real: '))
        except:
            n=print('\033[0;31mVocê digitou uma opção inválida, tente de novo.\033[m')
        else:
            break
    return n
x=leiaint('')
y=leiaFloat('')
print('='*20)
print(f"Você digitou o inteiro {x} e o real {y}")

'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de 
tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''