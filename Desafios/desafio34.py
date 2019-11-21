print('-=-'*20)
print('\033[0;33;47mANALISANDO AS RETAS DOS TRIANGULO...\033[m')
print('-=-'*20)
reta = float(input('Digite o seguimento de reta1:'))
reta2 = float(input('Digite o seguimento de reta2:'))
reta3 = float(input('Digite o seguimento de reta 3:'))
calculo = reta<reta2+reta3 and reta2<reta+reta3 and reta3<reta+reta2
if calculo:
    print('O triângulo PODE SER FORMADO!')
else:
    print('O triângulo NÃO PODE SER FORMADO!')