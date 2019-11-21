'''catop = float(input('Qual a medida do cateto oposto?'))
catadj = float(input('Qual a medida do cateto adjacente?'))
calculo = (catop**2 + catadj**2) ** (1/2)
print('O resultado dahipotenuza é {:.2f}:'.format(calculo))'''
import math
catop = float(input('Qual a medida do cateto oposto?'))
catadj =float(input('Qual a medida do cateto adj?'))
calculo = math.hypot(catop, catadj)
print('A hipotenuza vai medir {:.2f}'.format(calculo))
