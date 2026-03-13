#  Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.


# Create an empty dictionary to store all data.
aluno = dict()

# Ask the user for the student's name.
aluno['nome'] = str(input('Nome: '))
# Ask the user for the student's average.
aluno['media'] = float(input(f'Media de {aluno['nome']}: '))

# if the student's average is sevem or higher, the pass!
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'

# if the student's average is greater than 5 and less than 7 , they are is recovery.
elif 5 <= aluno['media'] <= 7:
    aluno['situacao'] = 'Recuparacao'
    
# Otherwise, the student is failed.
else:
    aluno['situacao'] = 'Reprovado'


for keys, valores in aluno.items():
    print(f'{keys} é igual a {valores}')