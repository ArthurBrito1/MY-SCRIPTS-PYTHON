temperatura = 0
media = 0
quanti = 0
while temperatura != 999:
    temperatura = int(input('Digite um numero ou 999 para sair: '))
    if temperatura != 999:
        media =  media + temperatura
        quanti = quanti + 1
print('Você dogotou {} numeros ea soma entre eles foi {}!'.format(quanti,media))
