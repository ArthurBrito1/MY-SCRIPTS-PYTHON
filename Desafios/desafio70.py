soma = 0
maisde1000 = 0
produt = ''
cont = 0
menos = 0
while True:
    nome = str(input('NOME DOPRODUTO:'))
    preço = float(input('PREÇO: R$'))
    soma = soma + preço
    if preço > 1000:
        maisde1000 = maisde1000 + 1
    if preço < 10:
        menos = preço
        produt = nome
    decisao =' '
    while decisao not in 'SN':
        decisao = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if decisao =='N':
            break
print('O totalde compra foi R${}'.format(soma))
print('Temos {} produtos custando mais de R$1000.00'.format(maisde1000))
print('O produto mais barato foi {} que custa R${} '.format(produt, menos))
