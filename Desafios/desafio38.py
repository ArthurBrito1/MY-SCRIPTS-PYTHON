num1 = int(input('Digite um numero:'))
num2 = int(input('Digiteo segundo numero:'))
if num1 > num2:
    print('\033[0;36;43mO PRIMEIRO numero é maior!\033[m')
elif num2 > num1:
    print('\033[0;36;43mO SEGUNDO numero é maior!\033[m')
elif num1 == num2:
    print('Não existe valor maior ou menor,\033[0;36;43m eles são IGUAIS!\033[m')
