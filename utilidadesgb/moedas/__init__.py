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

def aumentar (pre, porcent):
	pre += pre * porcent/100
	return moeda(pre)
	
def diminuir (pre, porcent):
	pre -= pre * porcent/100
	return moeda(pre)
	
def dobro (pre):
	pre *= 2
	return moeda(pre)
	
def metade (pre):
	pre = pre / 2
	return moeda(pre)
	
def moeda (pre):
	#preço formatado
	preF = str(f'R$ {pre:.2f}').replace('.', ',')
	return preF
	
def resumo (pre, vA, vD):
	print(f'{"-" * 56}\n{"RESUMO DO VALOR":^56}\n{"-" * 56}\n{"Preço analisado:":<38}{moeda(pre)}\n{"Dobro do preço:":<38}{dobro(pre)}\n{"Metade do preço:":<38}{metade(pre)}\n{"80% de aumento:":<38}{aumentar (pre, vA)}\n{"35% de redução:":<38}{diminuir(pre, vD)}\n{"-" * 56}')