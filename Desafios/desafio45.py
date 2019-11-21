import random
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = random.randint(0,2)
print('''SUAS OPÇÕES
[ 0 ] Pedra:
[ 1 ] Papel:
[ 2 ] Tesoura:''')
jogador = int(input('Qual sua opção? '))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!!')
sleep(1)
print('='*30)
print('O jogador jogou {}'.format(itens[jogador]))
print('O computador jogou {}'.format(itens[computador]))
print('='*30)
if jogador == 0 and computador == 0:
    print('EMPATE!')
elif jogador == 1 and computador == 1:
    print('EMPATE!')
elif jogador == 2 and computador == 2:
    print('EMPATE!')
elif jogador == 0 and computador == 2:
    print('JOGADOR GANHOU!')
elif jogador == 1 and computador == 0:
    print('JOGADOR GANHOU!')
elif jogador == 2 and computador == 1:
    print('JOGADOR GANHOU!')
else:
    print('O COMPUTADOR GANHOU!')
