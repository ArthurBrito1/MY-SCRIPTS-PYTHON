from datetime import date
ano = int(input('Digite o seu ano de nascimento:'))
sexo = str(input('Digite seu sexo:'))
datatual = date.today().year
idade = datatual - ano
anodealistamento = ano + 18
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, datatual))
if sexo == 'mulher':
    print('Não é necessario o alistamento obrigatorio!')
elif idade < 18:
    alistamento2 = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(alistamento2))
    print('Seu alistamento será em {}'.format(anodealistamento))
elif idade > 18:
    alistamento3 = datatual - anodealistamento
    print('Voçê ja deveria ter se alistado há {} anos'.format(alistamento3))
    print('A data do seu alistamento foi em {}'.format(anodealistamento))
elif idade == 18:
    print('Voçê deve se alistar IEDIATAMENTE!')
