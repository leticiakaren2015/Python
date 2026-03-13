# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Digite o angulo que você deseja:'))
se = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, se))
co = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, co))
ta = tan(radians(angulo))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, ta))
