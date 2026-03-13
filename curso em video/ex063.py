# Escreva um programa que leia um número N inteiro qualquer e mostre na tela 
# os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
0 - 1 - 1 - 2 - 3 - 5 - 8

número = int(input("Quantos termos você quer mostrar? "))
termo1 = 0 
termo2 = 1
print(f"{termo1} -> {termo2}", end="")
cont = 3
while cont <= número: 
    termo3 = termo1 + termo2
    print(f" -> {termo3}", end="")
    cont += 1
    termo1 = termo2
    termo2 = termo3
print(" -> FIM")


