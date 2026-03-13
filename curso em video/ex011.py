# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrado.

width = float(input('wall width: '))
height = float(input('wall height: '))
area = width * height
print('your wall has the dimension from {}x{} end your area it is from {}m².'.format(width, height, area))
ink = area / 2.5
print('for paint this wall, you will need  {:.2f}l of ink.'.format(ink))
