velocidade = float(input('digite sua velocidade em km/h:'))
multa = (velocidade-80)*7
if velocidade>80:
    print('Tu vai morrer mizera diminui a velocidade!!! por que tua multa hooje vai ser R${:.2f}'.format(multa))
else:
    print('Parabéns voçê é m motorista exemplar!')