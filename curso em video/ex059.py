# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso


# Usando a biblioteca tempo
from time import sleep


num1 = float(input('digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

# Loop principal
while True:
    print("===" * 10)
    sleep(2)
    print('''MENU PRINCIPAL:\n
[ \033[30:42m1\033[m ] Somar
[ \033[30:43m2\033[m ] Mutiplicar
[ \033[30:44m3\033[m ] Maior
[ \033[30:45m4\033[m ] Novo número
[ \033[30:46m5\033[m ] Sair do programa\n''')

    opção = int(input('>>>Escolha uma das opções ACIMA: '))

    # Caso escolha opção 1
    if opção == 1:
        soma = num1 + num2
        print("\033[32mA soma entre {} + {}  é igual a {}\033[m".format(num1, num2, soma))

    # Caso escolha opção 2
    elif opção == 2:
        mult = num1 * num2
        print("\033[33mO resultado de {} X {}  é igual a {}\033[m".format(num1, num2, mult))

    # Caso escolha opção 3
    elif opção == 3:
        if num1 > num2:
            print("\033[34m Entre o número {} e {}, o número {} é MAIOR.\033[m".format(num1, num2, num1))
        elif num2 > num1:
            print("\033[34m Entre o número {} e {}, o número {} é MAIOR.\033[m".format(num2, num1, num2))
        else:
            print("\033[34mO dois números são iguais😛\033[m")

    # Caso escolha opção 4
    elif opção == 4:
        num1 = float(input('digite o primeiro valor: '))
        num2 = float(input('Digite o segundo valor: '))

    # Caso escolha opção 5
    elif opção == 5:
        print("\033[32mFinalizando...\033[m")
        sleep(1.5)
        print("\033[33mAguade...\033[m")
        sleep(1.5)
        print("\033[34mThanks you!\033[m")
        print("\033[35mAté logo! 🤗🤗🤗🤗\033[m")
        break  # Sair do loop

    # Caso escolha opção inválida
    else:
        print("\033[31mOpeção inválida. Tente novamente!\033[m\n")
