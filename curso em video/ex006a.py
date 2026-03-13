# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('write a number?'))
print('the double {} is {},'.format(n, (n*2)))
print('the triple {} is {}, and it is square root {} is {:.1f}.'.format(n, (n*3), n, pow(n, (1/2))))
