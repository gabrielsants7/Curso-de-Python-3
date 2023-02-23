
def moeda(p, moeda='R$'):
    return '{}{:.2f}'.format(moeda, p).replace('.',',')  
    
def metade(p):
    res = moeda(p / 2)
    return res
    
def dobro(p):
    res = moeda(p * 2)
    return res
    
def aumento(p):
    res = moeda(p + (p * 10/100))
    return res