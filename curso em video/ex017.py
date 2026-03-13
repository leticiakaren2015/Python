# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

"""co = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o cateto adjecente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))"""

from math import hypot
co = float(input('Comprimento do cateto opsto:'))
ca = float(input('Comprimneto do cateto adjecente:'))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
