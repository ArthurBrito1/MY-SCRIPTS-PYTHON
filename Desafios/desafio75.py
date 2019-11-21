n1 = (int(input('Digite um numero:')),
    int(input('Digite outro numero:')),
    int(input('Digite mais um numero:')),
    int(input('Digite o ultimo numero:')))
print('Os numeros digitaos foras {}'.format(n1))
print('O valor 9 apareceu {} vezes'.format(n1.count(9)))
if 3 in n1:
    print('O valor 3 está na posição {}'.format(n1.index(3)+1))
else:
    print ('Não existe numero 3')
for n in n1:
    if n%2==0:
        print('Os valores pares digitados foram {}'.format(n))