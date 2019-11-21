salario = float(input('Digite seu salario, voçê receberá um aumento.'))
aumento = salario + (salario*15/100)
aumento2 = salario + (salario*10/100)
if salario <= 1250:
    print('salario novo sera R${:.2f}'.format(aumento))
else:
    print('Novo salario será R${:.2f}'.format(aumento2))
