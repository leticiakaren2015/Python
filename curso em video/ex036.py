# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Qual o valor da casa? "))
salário = float(input("Qual o seu salário? "))
anos = int(input("Quantos anos? "))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print("Para pagar uma casa de R${:.2f} em {} anos ".format(casa, anos), end="")
print("A prestação da casa será de R${:.2f}".format(prestação))
if prestação <= mínimo:
    print("Empréstimo APROVADO!")
else:
    print("Empéstimo NEGADO!")
