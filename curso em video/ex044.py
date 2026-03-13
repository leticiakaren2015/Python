  # Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print("{:^40}".format(" \033[33mLOJAS OLIVEIRAS\033[m "))

preço = float(input("Digite o valor das compras: R$ "))
pagamento = []

while True:
    print("\nEscolha uma das opções: ")
    print("\033[7;36m1\033[m. À vista dinheiro/cheque")
    print("\033[7;32m2\033[m. À vista no cartão")
    print("\033[7;33m3\033[m. Até 2X no cartão")
    print("\033[7;34m4\033[m. 3X ou mais no cartão")
    print("\033[7;35m5\033[m. Sair")

    opção = input("Digite sua forma de pagamento (1/2/3/4/5): ")

    if opção == "1":
        total = preço - (preço * 10 / 100)
        print("""\033[36mParabés você ganhou 10% de desconto!
Sua compra de R${:.2f} vai custar R${:.2f} no final.\033[m""".format(preço, total))
    elif opção == "2":
        total = preço - (preço * 5 / 100)
        print("""\033[32mParabés você ganhou 10% de desconto!
Sua compra de R${:.2f} vai custar R${:.2f} no final.\033[m""".format(preço, total))
    elif opção == "3":
        total = preço
        parcela = total / 2
        print("\033[33mSua compra será parcelada em 2x de R${:.2f} SEM JUROS.\033[m".format(parcela))
        print("\033[33mSua compra de R${:.2f} vai custar R${:.2f} no final.\033[m".format(preço, total))
    elif opção == "4":
        total = preço + (preço * 20 / 100)
        total_de_parcela = int(input("\033[1;33;40mQuantas parcelas?\033[m "))
        parcela = total / total_de_parcela
        print("\033[34mSua compra será parcelada em {}x de R${:.2f} COM JUROS.\033[m".format(total_de_parcela, parcela))
        print("\033[34mSua compra de R${:.2f} vai custar R${:.2f} no final.\033[m".format(preço, total))
    elif opção == "5":
        print("\033[35mEncerrando o programa. Até logo!\033[m")
        break
    else:
        print("\033[31mOpção inválida. Por favor, escolha novamente\033[m")
