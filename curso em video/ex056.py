#  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
#  mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


soma_idade = 0
média_idade = 0
maior_idade_do_homem = 0
nome_velho = " "
total_mulher = 0

for p in range(1, 5):
    print("\033[35mColeta de dados da {}ª pessoa\033[m".format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    soma_idade += idade

    if p == 1 and sexo in "Mm":
        maior_idade_do_homem = idade
        nome_velho = nome

    if sexo in "Mm" and idade > maior_idade_do_homem:
        maior_idade_do_homem = idade
        nome_velho = nome

    if sexo in "Ff" and idade < 20:
        total_mulher += 1

média_idade = soma_idade / 4
print("\033[34mA média da idade do grupo é {} anos.\033[m".format(média_idade))
print("\033[33mO nome do homen mais velho é {}.\033[m".format(nome_velho))
print("\033[31mTotal de mulheres 🧍‍♀️ com menos de 20 anos é {}\033[m".format(total_mulher))
