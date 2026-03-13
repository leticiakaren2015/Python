# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


listanun = list()

maior = 0
menor = 0

for c in range(0, 5):
    listanun.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        maior = menor = listanun[c]
    else:
        if listanun[c] > maior:
            maior = listanun[c]
        if  listanun[c] < menor:
            menor = listanun[c]
print('-=' * 30)
print(f'Os número digitados foram {listanun}')

print(f'O maior valor digitado foi {maior} na posição ', end='')
for indice, valor in enumerate(listanun):
    if valor == maior:
        print(f'{indice}...', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for indice, valor in enumerate(listanun):
    if valor == menor:
        print(f'{indice}...', end='')
print()
