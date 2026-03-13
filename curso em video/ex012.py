# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.

product = float(input('Price of the product? R$'))
desc = product-(product * 5 / 100)
print('your product with discount de 5 % will be R${:.2f}.'.format(desc))
