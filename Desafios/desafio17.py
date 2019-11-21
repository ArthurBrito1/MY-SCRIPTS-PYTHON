import math
angulo = int(input('Digite o ângulo que voçe quer:'))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('o angulo de {} tem: \n seno:{:.2f} \n coseno:{:.2f} \n tangente:{:.2f}'.format(angulo, seno, coseno, tangente))