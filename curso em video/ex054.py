#  Crie um programa que leia o ano de nascimento de sete pessoas. No final,
#  mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
totmaior = 0
totmenor = 0
atual = date.today().year

for pess in range(1, 8):
    nasc = int(input("E que ano a {}º pessoa nasceu?: ".format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print("Ao todos tivemos {} pessoas maiores de idade.".format(totmaior))
print("E também tivemos {} pessoas menores de idade.".format(totmenor))
