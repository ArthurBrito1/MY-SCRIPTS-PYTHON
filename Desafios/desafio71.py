print('=-'*25)
print(' '*15,'BANCO DO ART',' '*15)
print('=-'*25)
valor = int(input('Que valor voçê deseja sacar? R$'))
tota = valor
ced = 50
cedtotal = 0
while True:
    if tota>=ced:
        tota = tota - ced
        cedtotal = cedtotal+1
    else:
        if cedtotal > 0:
            print('Total de {} cédulas de R${}'.format(cedtotal, ced))
        if ced ==50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cedtotal = 0
        if tota == 0:
            break
print('-'*25)
print(' '*5,'VOLTE SEMPRE',' '*5)
print('-'*25)