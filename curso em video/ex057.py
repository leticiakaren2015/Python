# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Qual o seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Resposta inválida! Qual o seu sexo [M/F]:  "))
idade = int(input("Qual sua idade: "))

if idade >= 18 and sexo in "Mm":
    sexo = "Mm"
    print("Você é um HOMEM ADULTO! 👨🏻")
if idade < 18 and sexo in "Mm":
    sexo = "Mm"
    print("Você é BEBÊ! 👶🏻")
if idade >= 18 and sexo in "Ff":
    sexo = "Ff"
    print("Você é um MULHER ADULTA! 👩🏻")
else:
    print("Você é uma BEBEZINHA! 👶🏻")
