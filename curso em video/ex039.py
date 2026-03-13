# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date


def verificar_alistamento():

    atual = date.today().year

    genero = str(input("diga-me seu gênero (homem / mulher): ")).strip().lower()

    if genero not in ["homem", "mulher"]:
        print("Gênero inválido. Por favor, digite 'homem' ou 'mulher'.")
        return

    try:
        nasc = int(input("Ano de nascimento. "))
    except ValueError:
        print("Ano de nascimento inválido. Por favor, digite um número inteiro.")
        return

    idade = atual - nasc
    print("Quem nasceu em {} tem {} anos em {}".format(nasc, idade, atual))

    if genero == "homem":
        if idade == 18:
            print("Você tem que se alistar IMEDIATAMENTE!")
        elif idade < 18:
            saldo = 18 - idade
            ano = atual + saldo
            print("Ainda falta {} anos para o alistamento".format(saldo))
            print("Seu alistamento será em {}".format(ano))
        elif idade > 18:
            saldo = idade - 18
            ano = atual - saldo
            print("Você deveria ter se alistado há {} anos.".format(saldo))
            print("Seu alistamento foi em {}.".format(ano))
    else:
        print("Fique tranquila você não precisa se ALISTAR :)")

if __name__ == "__main__":
    verificar_alistamento()
