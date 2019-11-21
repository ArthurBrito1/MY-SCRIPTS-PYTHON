from time import sleep
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite mais um numero:'))
opção = 0
while opção != 5:
    print('''    [ 1 ] SOMAR:
    [ 2 ] MULTIPLICAR:
    [ 3 ] MAIOR
    [ 4 ] NOVOS NUMEROS:
    [ 5 ] SAIR DO PROGRAMA!''')
    opção = int(input('>>>>>>Qualasua opção:'))
    if opção == 1:
        soma = numero1+numero2
        print('A soma entre {} e {} é {}!'.format(numero1, numero2, soma))
    elif opção == 2:
        multiplicar = numero1*numero2
        print('A multiplicação de {} e {} é {}!'.format(numero1, numero2, multiplicar))
    elif opção == 3:
        if numero1 > numero2:
            print('O numero {} é o maior!'.format(numero1))
        else:
            print('O numero {} é o maior!'.format(numero2))
    elif opção == 4:
        print('Informe os numeros novamente:')
        numero1 = int(input('Digite o primeiro valor:'))
        numero2 = int(input('Digite o segundo valor:'))
    elif opção == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção invalida. Tente novamente!')
print('Fim do programa!')
