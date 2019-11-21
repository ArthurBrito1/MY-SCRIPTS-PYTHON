frase = 'Arthur é lindo'
frase[0:6]
len(frase)
frase.count('o')
frase.count('o', 0, 13)
frase.find('lin')#mostra a posição onde esta#
frase.find('androide') #retorna -1 pq nãoexiste na frase#
'Arthur'in frase
frase.replace('lindo', 'Android') #substitui um pelo outro#
frase.upper() #transforma tudo em maiusculo#
frase.lower()  #transforma tudo em minusculo#
frase.capitalize() #deixa tudo em minusculo menos a primeira letra#
frase.title() #analisa quantas palavras tem na frase#
frase.strip() #remove espaços inuteis no inicio e final da str#
frase.rstrip() #remove somente osultios espaços#
frase.lstrip() #remove somente os primeiros espaços#
frase.split() #ocorre uma divisão na sua str considerando os espaços#
'-'.join() #junta uma str na outra#
