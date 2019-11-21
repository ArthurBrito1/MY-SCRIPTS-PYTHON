res = 'S'
cont = soma = media = maior = menor = 0
while res in 'Ss':
    num = int(input('Digite um numero: '))
    soma = soma+num
    cont = cont+1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma/num
print('Voçê digitou {}  e a soma entre eles é {} e a media é {}!'.format(cont, soma, media))
print(' o maior valor foi {} e o menor valor foi {}!'.format(maior, menor))
