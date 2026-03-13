# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print("{:^60}".format(" \033[34mVamos descobrir se o número é PRIMO!\033[m "))
num = int(input("Digite um número: "))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[33m", end="")
        total += 1
    else:
        print("\033[31m", end="")
    print("{} ".format(c), end="")
print("\n\033[mO número {} foi divisíevl {} vezes".format(num, total))
if total == 2:
    print(" E por isso ele é PRIMO")
else:
    print("E por isso ele NÃO é PRIMO")
