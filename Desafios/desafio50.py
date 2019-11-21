s = 0
cont = 0
for c in range(0,6):
        n = int(input('Digite um valor:'))
        if n % 2 == 0:
            s = s + n
            cont = cont + 1
print("Voçê informou {} numeros PARES e o somatorio desses valores foi {}".format(cont, s))
