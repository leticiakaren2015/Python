# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('write a number'))
d = n * 2
t = n * 3
r = n ** (1/2)
print(' the double {} is {},\n the triple {} is {} and \n it is square root {} is {:.2f} .'.format(n, d, n, t, n, r))
