print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
pt = int(input('Primeiro termo:'))
r = int(input('Razão:'))
dec = pt + (10-1)*r
for c in range(pt, dec+1, r):
    print('{}'.format(c), end=' >> ')
print('ACABOU')