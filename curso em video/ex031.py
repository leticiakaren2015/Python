#  Desenvolva um programa que pergunte a distância de uma viagem em Km.
#  Calcule o preço da passagem, cobrando R$0,50 por Km para
#  viagens de até 200Km e R$0,45 parta viagens mais longas.

distância = float(input("Qual a distância da sua viagem?  "))
print("você está preste a cmeçar uma viagem de {}km.".format(distância))
if distância <= 200:
    preço: float = distância * 0.50
else:
    preço = distância * 0.45
print("É o preço da sua passagem será de {:.2f}".format(preço))
