tempo = int(input())
quantidade_seg = [3600, 60, 1]
resultado = []
for isso in quantidade_seg:
    quantidade = int(tempo / isso)
    resultado.append(str(quantidade))
    tempo -= quantidade * isso
print(":".join(resultado))

'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, 
e informe-o expresso no formato horas:minutos:segundos.
'''