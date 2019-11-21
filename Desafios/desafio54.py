from datetime import date
ano = date.today().year
totalmaior = 0
totalmenor = 0
for pessoas in range(1, 7+1):
    nascimento = int(input('Em qual ano a {} pessoa nasceu?'.format(pessoas)))
    idade = ano - nascimento
    if idade >= 18:
        totalmaior = totalmaior + 1
    else:
        totalmenor = totalmenor + 1
print('No total temos {} pessoas MAIORE DE IDADE!\nE temos {} pessoas MENOR DE IDADE'.format(totalmaior, totalmenor))
