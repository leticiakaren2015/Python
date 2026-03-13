# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = mais_de_mil = menor = count = 0
barato = ' '
while True:
    produto = str(input('Digite o seu produto: '))
    preço = float(input('Digite o valor do seu produto: '))
    
    total += preço
    
    if preço > 1000:
        mais_de_mil += 1
    if count == 1 or preço < menor:
        menor = preço
        barato = produto


    continuar = ' '
    
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar != 'S':
        break

print(f'O total de compra foi R$ {total:.2f}')
print(f'Temos {mais_de_mil} produto(s) custando mais de R$1.000,00.')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')