num = int(input('Informe um número: '))+1000
strnum = str(num)
print(f'Analisando o número {num}')
print(f'Unidade: {strnum[3]}')
print(f'Dezena: {strnum[2]}')
print(f'Centena: {strnum[1]}')
print(f'Milhar: {int(strnum[0]) - 1}')