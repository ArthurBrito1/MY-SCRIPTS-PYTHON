temperatura = 0
media = 0
quanti = 0
while temperatura != 999:
    temperatura = int(input('Digite a temperatura ou 999 para sair: *C'))
    if temperatura != 999:
        media =  media + temperatura
        quanti = quanti + 1
r= media/quanti
print(r)
