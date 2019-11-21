cont = 0
soma = 0
while True:
    n = int(input('Digite um numero (999 para parar):'))
    if n == 999:
        break
    cont = cont + 1
    soma = soma+n
print('A soma dos {} valres foi {}!'.format(cont,soma))
