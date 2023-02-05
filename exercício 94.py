DadosPessoas = list()
ContagemPessoas = SomaIdades = SexoFeminino = 0
while True:
    Informacoes = dict()
    Informacoes["Nome"] = str(input('Nome: ')).strip().title()
    while len(Informacoes["Nome"]) == 0:
        Informacoes["Nome"] = str(input('Nome: ')).strip().title()
    Informacoes["Sexo"] = str(input('Sexo [M/F]: ')).strip().lower()[0]
    while Informacoes["Sexo"] != 'm' and Informacoes["Sexo"] != 'f':
        Informacoes["Sexo"] = str(input('Sexo [m/f]: ')).strip().lower()[0]
    Informacoes["Idade"] = int(input('Idade: '))
    while Informacoes["Idade"] < 0 or Informacoes["Idade"] > 150:
        Informacoes["Idade"] = int(input('Idade: '))
    DadosPessoas.append(Informacoes)
    ContagemPessoas += 1
    if Informacoes["Sexo"] == 'f':
        SexoFeminino += 1
    SomaIdades = SomaIdades + Informacoes["Idade"]
    Continuar = str(input('Quer continuar? [s/n] ')).strip().lower()
    while Continuar != 's' and Continuar != 'n':
        Continuar = str(input('Quer continuar? [s/n] ')).strip().lower()
    print('--' * 30)
    if Continuar == "n":
        break
MediaIdades = SomaIdades/ContagemPessoas
print('A) Foram cadastradas {} pessoas;'.format(ContagemPessoas))
print('B) A média das idades cadastradas é {:.2f} anos;'.format(MediaIdades))
if SexoFeminino > 0:
    print('C) As mulheres cadastradas foram:')
    print('--' * 30)
    for c in DadosPessoas:
        if c["Sexo"] == 'f':
            print(f'    -> {c["Nome"]}')
    print('--' * 30)
else:
    print('C) Não foram cadastradas pessoas de sexo feminino;')
print("D) Pessoas com idade acima da média: ")
print('--' * 30)
ContagemPessoas = 0
for c in DadosPessoas:
    if c["Idade"] > MediaIdades:
        print(f'    -> {c["Nome"]}, sexo {c["Sexo"].upper()} e idade {c["Idade"]}')
        ContagemPessoas += 1
if ContagemPessoas == 0:
    print('     -> Não há pessoas com idade acima da média!')
print('--' * 30)
print('*** FIM DO PROGRAMA *****')

'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário 
e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''