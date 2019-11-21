#ex
carro.siga() #faz o carro ir para frente
if carro.esquerda(): #condiçâo caso o carro va para a esquerda bloco verdadeiro
#ele ira fzr isto
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
elif carro.direita: #condição caso ocarro não vire a esquerda bloco falso
#ele ira fzr
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
elif carro.ré():
    #vai para atrás
    carro.atras()
else:
#segue em frente
    carro.siga()
carro.pare()