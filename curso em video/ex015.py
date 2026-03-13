# Escreva um programa que pergunte a quantidade de Km percorridos por um
# carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar,sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('number of km traveled ?'))
days = int(input('number or days rented?'))
km = km * 0.15
days = days * 60
total = km + days
print('you will pay value is R${:.2f} for km wheeled and  R${:.2f} for days rented.'.format(km, days))
print('total payable  R${:.2f}'.format(total))
 