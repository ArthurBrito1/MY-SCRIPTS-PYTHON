viagem = int(input('Digite a distancia da viagem em KM:'))
preço = 0.50*viagem
preço2 = 0.45*viagem
print('-==-'*20)
print('\033[0;33;47mPara viagens de ate 200KM será cobrado R$0,50 por KM\033[m\n \033[0;33;47mE para vieagens de masi de 200KM sera cobrado R$0,45\033[m')
print('-==-'*20)
if preço<=200:
    print('A viagem de \033[32m{} será R$\033[33m{}'.format(viagem, preço))
else:
    print('A viagem de {} será R${}'.format(viagem, preço2))