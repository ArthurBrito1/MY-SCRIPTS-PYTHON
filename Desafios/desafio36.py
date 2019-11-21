valor = float(input('Digite o valor da casa em R$:'))
salário = float(input('Digite o seu salario em R$:'))
anos = int(input('Em quantos anos voçê quer pagar essa casa?'))
prestação = valor/(anos*12)
if prestação <= salário*30/100:
    print('EMPRESTIMO CONCEDIDO! \nPagará R${:.2f} por mês.'.format(prestação))
else:
    print('Voçê não pode finaciar a casa pois seu salárario é de R${} e voçê teráque pagar R${} por mês. \nEMPRESTIMO NEGADO!'.format(salário, prestação))
