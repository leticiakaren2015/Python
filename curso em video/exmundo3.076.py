# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, 
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)
listagem = ('lápis', 1.75,
            'borracha', 2,
            'caderno', 15.90,
            'estojo', 30.04,
            'transferidor', 4.20,
            'compasso', 9.99,
            'mochila', 200.15,
            'canetas', 22.30,
            'livro', 34.90)

for posição in range(0, len(listagem)):
    if posição % 2 == 0:
        print(f'{listagem[posição]:.<30}',end='')
    else:
        print(f'{listagem[posição]:>7.2f}')

