nome = str(input('Digite seu nome completo:')).strip()
divisão = nome.split()
print('Prazer em te conhecer!')
print('Seu primero nome é {}'.format(divisão[0]))
print('Seu ultimo nome é {}'.format(divisão[len(divisão)-1]))