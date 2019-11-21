numero = 0
de0a25 = 0
de26a50 = 0
de51a75 = 0
de76a100 = 0
while numero>=0:
    numero = int(input('Digite um numero ou um numero negativopara sair:'))
    if numero >= 0:
        if numero <=25:
            de0a25 = de0a25 + 1
        else:
            if numero <= 50:
                de26a50 = de26a50 + 1
            else:
                if numero <= 75:
                    de51a75 = de51a75 + 1
                else:
                    if numero <= 100:
                        de76a100 = de76a100 + 1
print('Temos {} numero entre 0 e 25'.format(de0a25))
print('Temos {} numero entre 26 e 50'.format(de26a50))
print('Temos {} numero entre 51 e 75'.format(de51a75))
print('Temos {} numero entre 76 e 100'.format(de76a100))
