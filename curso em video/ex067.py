#Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.


while True:
    num = int(input("Digite um número pra ver sua tabuada de multiplicar: "))
    print("_" * 60)
    if num < 0:
        break
    
    for c in range (1,11):
        print(f"{num} X {c} = {num * c}")
    print ("_" * 60)
print("Programa encerrado!")    