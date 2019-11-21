import random
nome1 = input('Digite o seu nome:')
nome2 = input('Digite o seu nome:')
nome3 = input('Digite o seu nome:')
nome4 = input('Digite o seu nome:')
lista = [nome1, nome2, nome3, nome4]
roleta = random.choice(lista)
print('O aluno escolhido foi {}'.format(roleta))
