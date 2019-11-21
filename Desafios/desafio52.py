numero = int(input('Digite um numero:'))
tot = 0
for c in range(1,numero+1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        tot = tot + 1
    else:
        print('\033[35m',end=' ')
    print('{}'.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(numero,tot))
if tot == 2:
    print('Ele é um numero PRIMO!')
else:
    print('Ele não é um numero PRIMO!')