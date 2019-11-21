nome = input('Digite o nome do aluno:')
materia = input('Digite a mateia:')
unidade1 = float(input('Digite a nota da primera unidade:'))
unudade2 = float(input('Digite a nota da segunda uniade:'))
unidade3 = float(input('Digite a nota da terceira unidade:'))
unidade4 = float(input('Digite a nota da quarta unidade:'))
mediadoaluno = (unidade1+unudade2+unidade3+unidade4)/4
print('O aluno {} tem como media final {:.2f} em {}!'.format(nome, mediadoaluno,materia))

