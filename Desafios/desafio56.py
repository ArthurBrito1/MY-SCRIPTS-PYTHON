somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomedomaisvelho = ''
totmulher20 = 0
for p in range(1,5):
    print('-----PESSOA{}-----'.format(p))
    nome = str(input('NOME:')).strip()
    idade = int(input('IDADE:'))
    sexo = str(input('[M/F]')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomedomaisvelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomedomaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20+1
mediaidade = somaidade/4
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O home mais velho tem {} anose se chama {} '.format(maioridadehomem, nomedomaisvelho))
print('Ao todo são {} mulhers com menos de 20 anos'.format(totmulher20))