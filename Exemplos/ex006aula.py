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
else(): #condição caso ocarro não vire a esquerda bloco falso
#ele ira fzr
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.pare()
