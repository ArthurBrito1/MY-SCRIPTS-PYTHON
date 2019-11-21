sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dadosivalidos por favor informe seu sexo:')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
