# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas. 
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# Inicializar lista para armazenamentos de dados
temporaria = [] # lista temporária para armazenar nome e peso
principal = [] # lista principal para armazenar todos os cadastrados
maior = menor = 0 # variáveis para armazenar valores máximo e mínimo


while True:
    try:
        # Request the name from the user validate if it contains only letters.
        while True:
            
            nome = str(input('Nome: ')).split()
            if nome and all(c.isalpha() or c.isspace() for c in nome):
                break
            print('Entrada inválida! O nome não pode conter números ou estar vazio.')
            
            # Request the user's weight and validate the entry.
            peso = float(input('Peso: '))  # Convert the weight input to float
            
            # Store the values in the temporária list
            
            temporaria.append(nome) 
            temporaria.append(peso)
            
            # If it's the first entry, define the fist weight with higher and lower weight.
            if len(principal) == 0:
                maior = menor = peso
            else: 
                # Updates the highest weight if a new higher value is found.
                if peso > maior:
                    maior = peso
                
                # Update the a lowest weight if a new lower value is found.
                if peso < menor:
                    menor = peso

            # Adds the data to the main list and clears the temporária list.
            principal.append(temporaria[:])
            temporaria.clear()
        
    except ValueError:
        #
        print('Entrada inválida! Certifique-se de digitar um número válido para peso.')
        continue
        
    
    resposta = str(input('Quer continuar? [S/N]  ')).strip().upper()
    
    while resposta not in ('S', 'N'):
        print("Resposta inválida! Digite 'S' para Continuar ou 'N' para Sair.")
        resposta = str(input('Quer continuar? [S/N]  ')).strip().upper()
        
    if resposta == 'N':
        break

print('-=' * 30)
print(f'Ao todo você cadastrou {len(principal)} pessoas. ')

print(f'O maior peso foi {maior}kg peso de ', end='')
for pessoa in principal:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end='')
print()

print(f'O menor peso foi {menor}kg peso de ', end='')
for pessoa in principal:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end='')
print()    
