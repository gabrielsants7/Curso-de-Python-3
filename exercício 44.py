print('========== LOJAS GUANABARA ==========')
preço = int(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção: '))
if opção == 1:
    desconto = preço * 10 / 100
    print(f'Sua compra de R${preço}  vai custar {preço - desconto:.2f} no final')
elif opção == 2:
    desconto = preço * 5 / 100
    print(f'Sua compra de R${preço} vai custar { preço - desconto:.2f} no final')
elif opção == 3:
    parcela = preço / 2
    print(f'Sua compra será parcelada em 2x de {parcela} SEM JUROS')
elif opção == 4: 
    parcelas = int(input('Quantas parcelas? '))
    valor_parcelado = preço / parcelas + preço * 20 / 1000
    print(f'Sua compras será parcelada em {parcelas}x de R${valor_parcelado:.2f} COM JUROS')
    juros = preço * 20 / 100
    print(f'Sua compra de R${preço:.2f} vai custar R${preço + juros:.2f} no final.')
else: 
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente')
    print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')

