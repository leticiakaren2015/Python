# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais


primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))
if primeiro > segundo:
    print("\033[33mO PRIMEIRO número é maior!\033[m")
elif primeiro < segundo:
    print("\033[34mO SEGUNDO número é maior\033[m!")
else:
    print("\033[36mNão existe valor maior, os doi são IGUAIS!\033[m")
