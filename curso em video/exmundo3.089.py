# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar 
# as notas de cada aluno individualmente.

# Criar uma lista vazia para armazenar  os dados de todos os estudantes.
# Creates an empty list to store all  student data.

ficha = list()

# Laco infinito para cadastrar os alunos.
# Infinite loop to register students.
while True:
    # Reads the student's name.
    nome = str(input('Nome: ')) 
    
    #Reads the first  grade.
    nota1 = float(input('Nota 1: '))
    
    # Reads the second grade.
    nota2 = float(input('Nota 2: '))
    
    # Calculates the average  of the two grades
    media = (nota1 + nota2) / 2
    
    # Adicionar dados do aluno a lista: nome, lista de notas, e media.
    # Adds student data to the list: name, grades list, and average
    ficha.append([nome, [nota1, nota2], media])
    
    # Asks if the user wants to continue and converts to uppercase
    resposta = input('Quer continuar? [S/N] ').upper()
    
    # if the answer is 'N', the loop is stopped.
    if resposta == 'N':
        break
    
# Print a decorative line
print('-=' * 30)

# Table header: number, name, and average
print(f'{"N°":<4}{"NOME":<10}{"MEDIA":>8}')

# Another decorative line.
print('-=' * 26)

# Percorre a lista de estudante com índice.
# Loop through the student list with index.
for i, a in enumerate(ficha):
    
    # Prints the index, student name, and average with 1 decimal
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
    
# laco para consultar notas de estudantes individual.
# loop for individual student grade queries.
while True:
    # Another decorative line
    print('-' * 35)
    # Asks for the student number (index).
    opc = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
    # if the number is 999, the program ends.
    if opc == 999:
        print('Finalizando...')
        break
    
    # verifica se o numero inserido corresponde para um estudante valido.
    # Checks if the entered number corresponds to a valid student.
    if opc <= len (ficha) -1:
        
        # Mostra o nome do estudante e suas notas.
        # Displays the student's name and their grades.
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
        
        # Mensagem de despedida amigável.
        # Friendly goodbye massage.
        print('<<<<VOLTE SEMPRE>>>>')