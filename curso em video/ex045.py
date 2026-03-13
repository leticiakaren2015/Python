from random import randint
from time import sleep

while True:

    itens = ("Pedra", "Papael", "Tesoura")
    computador = randint(0, 2)
    print("\033[37m-=\033[m" * 12)
    print("""\033[7;35mSuas opções:\033[m
[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA""")
    jogador = int(input("Qual é a sua jogada? "))
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PÔ!!!")
    sleep(1)
    print("\033[33m-=\033[m" * 12)
    print("Computador jogou {}".format(itens[computador]))
    print("Jogador jogou {}".format(itens[jogador]))
    print("\033[33m-=\033[m" * 12)

    if computador == 0:  # computador jogou PEDRA
        if jogador == 0:
            print("Impate!")
        elif jogador == 1:
            print("Jogador ganhou!")
        elif jogador == 2:
            print("Jogador perdeu!")
        else:
            print("JOGADA INVÁLIDA!")

    elif computador == 1:  # computador jogou PAPEL
        if jogador == 0:
            print("Jogador perdeu!")
        elif jogador == 1:
            print("Impate!")
        elif jogador == 2:
            print("Jogador ganhou!")
        else:
            print("JOGADA INVÁLIDA!")

    elif computador == 2:  # computador jogou TESOURA
        if jogador == 0:
            print("Jogador ganhou!")
        elif jogador == 1:
            print("Jogador perdeu!")
        elif jogador == 2:
            print("Impate!")
        else:
            print("JOGADA INVÁLIDA!")
