import random
print('A maquina esta pensando em um numero de 0 a 10... adivinhe se for capaz hehehehe')
numero = random.randint(0,10)
print ('Digite um numero de 0 a 10 seuu lixo:')
acertou = False
palpites = 0
while not acertou:
    digite = int(input('Digite um numero seuu lixo:'))
    palpites = palpites + 1
    if digite > numero:
        print('O numero é MENOR SEU EMPRESTAVEL!')
    if digite < numero:
        print('O numero é MAIOR SEU INUTIL!')
    if digite == numero:
        acertou = True
print('ACERTOU COM {} TENTATIVAS HAHAHA SEU LIXO. Mas como eu sou muito adoravel vou deixar voçê passar...'.format(palpites))
