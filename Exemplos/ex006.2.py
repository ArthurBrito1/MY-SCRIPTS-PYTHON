"""nome = str(input('Qual é o seu nome?'))
if nome == 'Arthur':
    print('Que nome lindo voçê tem!')
else:
    print('Seu nome é tão norma!')
print('Bom dia! {}'.format(nome))"""
nota1 = float(input('Digite sua nota:'))
nota2 = float(input('Digite sua outra nota:'))
media = (nota1+nota2)/2
print('A sua media foi {:.1f}'.format(media))
if media>=6:
    print('Aprovado')
else:
    print('Reprovado')