# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

# Inicializa o número de palpites
palpite = 0
acertou = False
# Gera um número aleatório entre 0 e 10
computador = randint(0, 10)

# Mensagem inicial
print("Olá, eu sou seu comutador!")

# Loop principal do jogo
while True:
    # Solicita ao usuário se ele quer jogar
    resposta = input("Quer jogar um jogo comigo?[S/N] ").strip().upper()
    break

    # Apresentar o jogo!
    print("Acabei de pensar em um número entre 0 e 10.")
    print("Será se você consegui aivinhar qal foi?\n")

while not acertou:
    if resposta == "S":

        # Solicita o palpite do jogador
        jogador = int(input("Qual é o seu palpite?\n"))
        palpite += 1

        # Verifica se o palpite está correto
        if jogador == computador:
            acertou = True
            print("ACERTOU!")
            print("Acertou com {} tentativas. Parabéns!".format(palpite))
            break  # Sai do loop após acertar
        else:
            # Dá uma dica ao jogador
            if jogador < computador:
                print("Mais...Tente mais uma vez.\n")
            elif jogador > computador:
                print("Menos...Tente mais uma vez.\n")

    elif resposta == "N":
        # Mensagem de despedida se o jogador não quiser jogar
        print("Que pena,você não quis jogar comigo!😥")
        print("Até mais!")
        break  # Sai do loop e encerra o programa
    else:
        # Mensagem para respostas inválidas
        print("Resposta inválida. Por favor, digite 'S' para sin e 'N' para não.")
