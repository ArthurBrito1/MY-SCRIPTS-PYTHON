print('='*10,'LOJA ART','='*10)
compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque:
[ 2 ] À vista cartão:
[ 3 ] 2X no cartão:
[ 4 ] 3X no cartão ou mais:''')
opção = int(input('Qual a opção?'))
if opção == 1:
    desconto = compras-(compras*10/100)
    print('O preço deste produto agora é {} e voçê ganhou um desconto de 10%!'.format(desconto))
elif opção == 2:
    desconto2 = compras-(compras*5/100)
    print('O preço deste produto agora é {} e voçê ganhou um desconto de 5%!'.format(desconto2))
elif opção == 3:
    parcelas1 = compras/2
    print('Sua compra será parcelada em 2x de R${}, SEM JUROS'.format(parcelas1))
    print('Sua compra será de R${}'.format(compras))
elif opção == 4:
    quantas = int(input('Quantas parcelas?'))
    juros = compras+(compras*20/100)
    parcelas = juros / quantas
    print('Sua compra será parcelada em {}x de R${:.2f}, COM JUROS'.format(quantas, parcelas))
    print('Sua compra de {} vai custar {} no final.'.format(compras, juros))
else:
    totao = 0
    print('OPÇÃO INVALIDA DE PAGAMENTO, TENTE NOVAMENTE!')