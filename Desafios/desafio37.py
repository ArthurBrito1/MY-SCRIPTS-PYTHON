numero = int(input('Digite um numero inteiro qualquer:'))
print('''ESCOLHA UMA DAS BASES PARA CONVERSÃO:
[ 1 ] PARA CONVERTER PARA BINARIO:
[ 2 ] PARA CONVERTER PARA OCTAL:
[ 3 ] PARA CONVERTER PARA HEXADECIMAL:''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binario é igual a {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('{} converito para octal é igual a {}'.format(numero,oct(numero)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida tente novamente')
