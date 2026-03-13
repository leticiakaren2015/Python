# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print("==" * 20)
print("{:^40}".format(" 10 TERMOS DE UMA PA"))
print("==" * 20)
primeiro = int(input("digite o primeiro termo: "))
razão = int(input("digite a razão: "))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + 1, razão ):
    print("{}".format(c), end=" » ")
print("Acabou")
