confirmacao = 's'
lista=list()
while confirmacao in 's':
    num = int(input('Digite um valor: '))
    print('Valor adicionado com sucesso...')
    if num in lista:
        print(f'o numero {num} já existe na lista')
    else:
        lista.append(num)
    while True:
        confirmacao = str(input('Deseja continuar:[S/N]? ')).strip().lower()
        if confirmacao in 'sn':
            break
print('=-'*40)
print(f'Você digitou os valores {sorted(lista)}')

'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número 
já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, 
em ordem crescente. 
'''