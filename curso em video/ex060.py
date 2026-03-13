# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120


print("Vamos calcular o fatorial de um número!")
num = int(input("digite um número: "))
c = num
f = 1
print(" calculando {}! = ".format(num), end="")
while c > 0:
    print("{}".format(c), end="")
    print(" X " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print("{}".format(f))
