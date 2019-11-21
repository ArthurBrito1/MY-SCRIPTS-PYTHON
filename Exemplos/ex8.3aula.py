juros = float(input('Informe os juros ah pagar: '))
capital = float(input('informe o seu capital:'))
periodo = int(input('Informe o periodo de tempo a ser pago:'))
for n in range(0,periodo):
    capital = capital + (capital * (juros/100))
    print(capital)
