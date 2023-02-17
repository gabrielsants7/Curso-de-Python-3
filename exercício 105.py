def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicion = dict()
    tot = mai = men = 0
    for c in range(0, len(num)):
        if c == 0:
            mai = men = num[c]
        else:
            tot += 1
            if num[c] > mai:
                mai = num[c]
            if num[c] < men:
                men = num[c]
    média = sum(num)/len(num)
    dicion['total'] = tot+1
    dicion['maior'] = mai
    dicion['menor'] = men
    dicion['média'] = (f'{média:.2f}')
    if sit:
        if média >= 7:
            situação = 'BOA'
        elif 5 < média < 7:
            situação = 'RAZOÁVEL'
        else:
            situação = 'RUIM'
        dicion['situação'] = situação
    return dicion


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)

'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário 
com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
'''