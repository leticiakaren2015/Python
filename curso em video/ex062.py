# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.
#  Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#  mostrando os 10 primeiros termos da progressão usando a estrutura while.

print("{:^40}".format("Gerador de PA"))
print("=-" * 20)
primeiro_termo = int(input("Digite um número: "))
razão = int(input("digite uma razão: "))
termo = primeiro_termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo}-> ", end="")
        termo += razão
        cont += 1
    print("pausa")    
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Progressão finalizada com {total} termos mostrados.")
