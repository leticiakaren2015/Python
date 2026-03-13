#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('digite um número: '))
resultado = num % 2 # número devidido por 2, quero somente o resto da divisão
if resultado == 0:
    print('Esse número {} é PAR'.format(num))
else:
    print('Esse número {} é ÍMPAR'.format(num))
