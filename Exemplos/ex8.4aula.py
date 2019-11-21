somaidade = 0
mediadasidades = 0
homemmaisvelho = 0
nomedohomemaisvelho = ''
mulher20 = 0
for n in range(1,4+1):
    print('-----PESSOA{}-----'.format(n))
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('[M/F]:'))
    somaidade = somaidade + idade
    if n==1 and  sexo in 'M/m':
        homemmaisvelho = idade
        nomedohomemaisvelho = nome
    if sexo in 'M/n' and idade > homemmaisvelho:
        homemmaisvelho = idade
        nomedohomemaisvelho = nome
    if sexo in 'F/f' and idade < 20:
        mulher20 = mulher20 + 1
mediadasidades = somaidade/4
print('A média das idades é {}.'.format(mediadasidades))
print('O homem mais velho tem {} anos e se chama {}.'.format(homemmaisvelho, nomedohomemaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulher20))
