maior18=0
homem = 0
mulher20 = 0
while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    if idade >= 18:
        maior18 = maior18 + 1
    if sexo == 'M':
        homem = homem + 1
    if sexo == 'F' and idade < 20:
        mulher20 = mulher20 + 1
    decisao = ' '
    while decisao not in 'SN':
        decisao = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if decisao == 'N':
        break
print('Totatl de pessoas com mais de 18 anos: {}'.format(maior18))
print('Ao todo temos {} homens cadastrados'.format(homem))
print('E temos {} mulheres com menos de 20 anos'.format(mulher20))