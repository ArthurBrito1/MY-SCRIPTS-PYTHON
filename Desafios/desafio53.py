frase = str(input('Digite uma frase:')).strip().upper()
palavra = frase.split()
junta = ''.join(palavra)
iverso = ''
for letra in range(len(junta) - 1, -1, -1):
    iverso = iverso + junta[letra]
print('O o inverso de {} é inverso {}'.format(junta, iverso))
if iverso == junta:
    print('Temos um palindromo!')
else:
    print('Não é palindromo!')

