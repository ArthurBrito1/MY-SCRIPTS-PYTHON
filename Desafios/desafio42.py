print('-=-'*20)
print('\033[0;33;47mANALISANDO AS RETAS DOS TRIANGULO...\033[m')
print('-=-'*20)
reta = float(input('Digite o seguimento de reta1:'))
reta2 = float(input('Digite o seguimento de reta2:'))
reta3 = float(input('Digite o seguimento de reta 3:'))
if reta<reta2+reta3 and reta2<reta+reta3 and reta3<reta+reta2:
    print('UM triângulo PODE SER FORMADO', end='')
    if reta2 == reta2 == reta3:
        print('EQUILATERO!')
    elif reta != reta2 != reta3 != reta:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('UM triângulo NÃO PODE SER FORMADO!')