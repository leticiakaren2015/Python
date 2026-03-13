# Faça um programa que leia três números e mostre qual é o maior e qual o menor.

a = int(input(" Primeiro valor: "))
b = int(input(" Segundo valor: "))
c = int(input(" Terceiro valor: "))
# Verificando quem é o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("o menor valor é {}".format(menor))
print("maior valor é {}".format(maior))
