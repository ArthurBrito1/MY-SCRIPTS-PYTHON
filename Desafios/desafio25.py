frase = str(input('Digite uma frase:')).strip()
print('A letra A aparece {} vezes'.format(frase.lower().count('a')))
print('A primeira letra A apreceuna posicão {}'.format(frase.lower().find('a')))
print('A ultima letra A apareceu na posição {}'.format(frase.lower().rfind('a')))