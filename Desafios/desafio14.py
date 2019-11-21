dias = int(input('A quantidade de dias que o carro foi alugado:'))
kilometros = float(input('Quantidade de quilometros rodados:'))
pagamento = (dias*60) + (kilometros*0.15)
print('O valor a ser pago será de R${:.2f}'.format(pagamento))