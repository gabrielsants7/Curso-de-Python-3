primeiro = float(input('Primeiro segmento: '))
segundo = float(input('Segundo segmento: '))
terceiro = float(input('Terceiro segmento: '))
if (segundo+terceiro) > primeiro and (primeiro+terceiro) > segundo and (primeiro+segundo) > terceiro:
    if primeiro == segundo == terceiro:
        print('Os lados podem formar um triângulo EQUILÁTERO.')
    elif primeiro == segundo or primeiro == terceiro or segundo == terceiro:
        print('Os lados podem formar um triângulo ISÓCELES.')
    else:
        print('Os lados podem formar um triângulo ESCALENO.')
else:
    print('Os lados não poder fomar um triângulo.')