a = int(input('Digite o valor 1:'))
b = int(input('Digite o valor 2:'))
c = int(input('Digite o valor 3:'))
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('Omaior numero digotado foi {}'.format(maior))