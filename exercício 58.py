from random import randint
random = randint(0, 10)
resposta = int()
erros = 0
print(f'Advinhe o número e ganhe!')
while resposta != random:
    resposta = int(input(f'Digite seu palpite:  '))
    if resposta != random:
        erros +=1
        if resposta > random:
            print(f'Menos... tente novamente!')
        else:
            print(f'Mais... tente novamente!')
print(f'Você acertou com {erros+1} tentativas!')

'''
Melhore o jogo do exercício 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o  jogador
 vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.8
'''