'''co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}!'. format(hi))''' 
#Método simples

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto Adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa é {:.2f}!'.format(hi))
#Método math
