print('='*20)
print('GERADOR DE PA')
print('='*20)
pt = int(input('Primeiro termo:'))
r = int(input('Razão:'))
termo = pt
count = 1
total = 0
mais = 10
while mais != 0:
    total = termo + mais
    while count <= total:
        print('{} ->'.format(termo), end=' ')
        termo = termo + r
        count = count+1
    print('PAUSA')
    mais = int(input('Quantos termos mais voçê quer mostrar?'))
print('finalizada com {} termos mostrados'.format(total))
