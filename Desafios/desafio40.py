nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digita a segundanota:'))
media = (nota1+nota2)/2
print('Tirando {} e {}, a média do aluno é {}'.format(nota1, nota2, media))
if 4<= media >=5 :
    print('O aluno está de RECUPERAÇÃO!')
elif media<=3:
    print('O aluno está REPROVADO!')
elif media>=7:
    print('O aluno está APROVADO!')