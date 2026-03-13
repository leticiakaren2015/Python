# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = cont = maior = menor = media = 0
resposta = "S"
while resposta in "Ss":
    while True:
        try:
            numero = int(input("digite um número: "))
            break
        except ValueError:    
            print("OPÇÃO INVÁLIDA!")
            
    soma += numero
    cont += 1
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    while True:
        resposta = str(input("quer continuar? (S/N) ")).strip().upper()[0]
        if resposta in "SN":
            break
        else:
            print("OPÇÃO INVÁLIDA! Digite 'S' para continuar e 'N' para sair.")
        
media = soma / cont   
print(media)
print(soma)
print(f"maior número é {maior} e o menor número é {menor}")