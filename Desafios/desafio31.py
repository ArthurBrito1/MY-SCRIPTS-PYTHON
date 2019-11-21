from datetime import date
ano = int(input('Digite um ano que quer analisar? Digite 0 para o ano atual:'))
calculo = ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0
if ano == 0:
    ano = date.today().year
if calculo:
    print('ELE É BISSESTO!')
else:
    print('ELE NÃO É BISSESTO!')
