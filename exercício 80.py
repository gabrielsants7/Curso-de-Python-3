lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > max(lista):
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        for p, item in enumerate(lista):
            if n < item:
                lista.insert(p, n)
                print(f'Adicionado a posicao {p} da lista...')
                break
print(lista)

'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição 
correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''