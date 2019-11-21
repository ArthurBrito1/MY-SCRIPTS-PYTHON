maiorpeso = 0
menor = 0
for pessoas in range(1,5+1):
    peso = float(input('Peso da pessoa {}: '.format(pessoas)))
    if pessoas == 1:
        maiorpeso = peso
        menor = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de  {}KG'.format(maiorpeso))
print('O menor peso lido foi de {}KG'.format(menor))
