# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

# Creates a 3x3 matrix (list of lists), initially filled with zeros.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Loop to fill the matrix with values provided by the user.
for l in range(0, 3): # loops through matrix rows(0 to .2)
    for c in range(0, 3):# loops through matrix columns ( 0 to 2).
        # Asks the user to enter a value for position [l][c]
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

# Prints a separation line          
print('-=' * 30)

# Loop to display a formatted matrix.
for l in range(0, 3): # Loops through matrix rows.
    for c in range(0, 3): # loops through matrix columns
        # Displays the value centered in 5 spaces, without line break
        print(f'[{matriz[l][c]:^5}]', end='')
        # After each row, moves to the next line.
    print()