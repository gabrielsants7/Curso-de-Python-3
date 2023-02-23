def metade(num=0.0):
    return num / 2


def dobro(num=0.0):
    return num * 2


def aumentar(num=0.0, aum=0):
    aumento = ((num * aum) / 100) + num
    return aumento


def diminuir(num=0.0, aum=0):
    resultado = num - ((num * aum) / 100)
    return resultado


def moeda(num=0.0, moeda='R$'):
    return f'{moeda}{num}'.replace('.', ',')