numero01 = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Nove', 'Dez')
while True:
    numero = int(input('Digite um numero entre 0 e 10:'))
    if 0<=numero<=10:
        break
print('Voçê digitou o numero {}'.format(numero01[numero]))