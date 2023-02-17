def sistema(fun):
    while True:
        manualmsg = f'Acessando o manual do comando "{fun}"'
        if fun == 'fim':
            break
        print('\033[34m~' * len(manualmsg) + '~~')
        print(f' {manualmsg}')
        print('~' * len(manualmsg) + '~~\033[m')
        from time import sleep
        sleep(1)
        print(f'\033[30m')
        help(fun)
        print(f'\033[m')
        sleep(1)
        if fun != 'fim':
            msg = 'SISTEMA DE AJUDA PyHELP'
            print('\033[32m~' * len(msg) + '~~')
            print(f' {msg}')
            print('~' * len(msg) + '~~\033[m')
            fun = str(input('Função ou Biblioteca > '))


msg = 'SISTEMA DE AJUDA PyHELP'
print('\033[32m~' * len(msg) + '~~')
print(f' {msg}')
print('~' * len(msg) + '~~\033[m')
sistema(str(input('Função ou Biblioteca > ')))
msgfinal = 'ATÉ LOGO!'
print('\033[31m~' * len(msgfinal) + '~~')
print(f' {msgfinal}')
print('~' * len(msgfinal) + '~~\033[m')

'''
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai 
aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
'''