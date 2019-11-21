peso = float(input('QUAL É SEU PESO? (KG)'))
altura = float(input('QUAL É SUA ALTURA? (M)'))
calculo = peso/(altura**2)
print('O IMCdessa pessoa é de {:.2f}'.format(calculo))
if calculo<18.5:
    print('ABAIXO DO PESO!')
elif 18.5<=calculo<25:
    print('PESO IDEAL!')
elif 25<=calculo<30:
    print('SOBREPESO!')
elif 30<=calculo<40:
    print('OBESIDADE!')
elif calculo >40:
    print('OBESIDADE MÓRBIDA!')
