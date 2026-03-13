# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

mais18 = homem_cadastrado = mulheres_menos_de_20 = 0
while True:
    idade = int(input('digite sua Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo [M/F]: ')).strip().upper()[0]
        
        if idade >= 18:
            mais18 += 1
        elif sexo == 'M':
            homem_cadastrado += 1
        elif sexo == 'F':
            mulheres_menos_de_20 += 1

    continuar =' '  
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar != 'S':
        break

print(f'Têm {mais18} no total pessoas cadastradas com mais de 18 anos.') 
print(f'Têm {homem_cadastrado} homens que foram cadastrados.')   
print(f'Têm {mulheres_menos_de_20} mulheres com menos de 20 foram cadastradas.')        
