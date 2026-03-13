#  Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#  mostrando os 10 primeiros termos da progressão usando a estrutura while.


# Solicita ao usuário para digitar o primeiro termo da progressão aritmética (PA)
primeiro_termo = int(input("Digite o primeiro termo: "))

# Solicita ao usuário para digitar a razão da PA
razão = int(input("Digite uma razão: "))

# Inicializa a variável 'termo' com o valor do primeiro termo
termo = primeiro_termo

# Inicializa o contador 'cont' com 1
cont = 1

# Enquanto o contador 'cont' for menor ou igual a 10
while cont <= 10:
    # Imprime o termo atual da PA seguido de uma seta
    print(f"{termo} → ", end="")
    
    # Atualiza o termo atual adicionando a razão
    termo += razão
    
    # Incrementa o contador em 1
    cont += 1

# Após o loop, imprime "FIM" para indicar o final da sequência
print("FIM")
