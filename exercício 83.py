expressão = str(input('Digite uma expressão: '))
p1 = expressão.count('(')
p2 = expressão.count(')')
if expressão[0] == ')':
    print('Expressão errada')
else:
    print('Sua expressão está errada!') if p1 > p2 or p2 > p1 else print('Sua expressão está válida!')

'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá 
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''