'''ex
while not maçã:
    if chão:
        passo
    if buraco:
        pula
    if moeda:
        pega
pega'''

c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')

r = 's'
while r == 'S':
    n = int(input('Digite um valor:'))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')

n = 1
impar = par = 0
while n !=0:
    n = int(input('Digite um valor:'))
    if n % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
print('Voçê digitou {} numeros pares e {} numeros impares!'.format(par, impar))

