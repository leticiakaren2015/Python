# Desenvolva um programa que leia o comprimento de três retas e diga
# ao usuário se elas podem ou não formar um triângulo.


print("_="*20)
print(" Analizador de Triângulo")
print("_="*20)


def seguimento_de_reta(r1, r2, r3):

    # Verifica se a soma de quaisquer lado é menor que a soma do terceiro
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        return True
    else:
        return False


def main():
    print("Bem-vindo ao jogo de formação de triângulo!")

# Ler os comprimentos das três retas

    r1 = float(input("Primeiro seguimento: "))
    r2 = float(input("Segundo seguimento: "))
    r3 = float(input("Terceiro seguimento: "))

# Verificar se podem formar um triângulo
    if seguimento_de_reta(r1, r2, r3):
        print("Os seguimentos PODE FORMAR um triângulo!")
    else:
        print("Os seguimentos NÃO PODE FORMAR um triângulo!")

# Perguntar ao usuário se ele deseja jogar novamente

    jogar_novamente = input("Deseja tentar novamente? (s/n): ")

    if jogar_novamente == "s":
        main()
    else:
        print("Fim de jogo!")

# Iniciar o jogo


main()
