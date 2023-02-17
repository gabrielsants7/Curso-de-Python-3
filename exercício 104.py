def leiaint(txt):
    while True:
        print(txt, end='')
        num = input()
        if num.isnumeric() == False:
            print('\033[31mERRO! Digite um número inteiro válido.\033[30m')
        else:
            break
    return num


# programa principal:
n = leiaint('\033[30mDigite um número inteiro: ')
print(f'\033[34mVocê acabou de digitar o número {n}.')

'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, 
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')

'''