
# List to store the numbers
numeros = [[], []]


contador = 0

# loop to collect 7 values.

while contador < 7:
    try:
        valor = int(input(f'Digite o {contador+1}º número: '))
        numeros.append(valor)
        
        if valor % 2 == 0:
            numeros[0].append(valor)
        else:
            numeros[1].append(valor)
            
        contador +=1

    except ValueError:
        print('Por favor, digite um número inteiro válido.')

# Ordering the lists
numeros[0].sort()
numeros[1].sort()

# Displaying the results
print(f'Os números pares que foram digitados são:{numeros[0]}')
print(f'Os números ímpares que foram digitados são:{numeros[1]}')
