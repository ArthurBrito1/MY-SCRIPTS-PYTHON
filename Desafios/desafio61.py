print('='*20)
print('GERADOR DE PA')
print('='*20)
pt = int(input('Primeiro termo:'))
r = int(input('Razão:'))
termo = pt
count = 0
while count <= 10:
    print('{} ->'.format(termo), end=' ')
    termo = termo + r
    count = count+1
print('FIM')
