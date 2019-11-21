from random import randint
print('-='*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*20)
v = 0
while True:
    numero = int(input('Digite um numero'))
    computador = randint(0, 11)
    escolha = ' '
    total = numero+computador
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print('Voçê jogou {} eo computador jogou {}. Total de {}'.format(numero,computador,total),end=' ')
    print('DEU PAR' if total%2==0 else 'DEU IMPAR')
    if escolha == 'P':
        if total%2==0:
            print('Voçê VENCEU!')
            v =v+1
        else:
            print('Voçê PERDEU!')
            break
    elif escolha == 'I':
        if total%2==0:
            print('Voçê VENCEU!')
            v=v+1
        else:
            print('Voçê PERDEU')
    print('Vamos jogar novamente...')
print('GAME OVER! Voçê venceu {} vezes.'.format(v))
