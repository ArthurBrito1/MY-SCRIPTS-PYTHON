nome = str(input('Qual é seu nome?'))
if nome == 'Arthur':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessika Juliana':
    print('Que belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
