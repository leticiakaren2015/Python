# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

wallet = float(input('how much money do your have now?  R$ '))
dollar = wallet / 4.85
print('with R${:.2f} you can buy  US${:.2f}'.format(wallet, dollar))
