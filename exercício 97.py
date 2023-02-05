def escreva(txt):
    tamanho_frase = len(txt)
    print(f'~'*(tamanho_frase + 4))
    print(f'  {txt}  ')
    print(f'~'*(tamanho_frase + 4))


escreva('Eu sou o melhor')
escreva('Mesmo eu não sendo')
escreva('Mas em minha cabeça eu sou o melhor!')

'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e 
mostre uma mensagem com tamanho adaptável.
Ex: 
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~
'''