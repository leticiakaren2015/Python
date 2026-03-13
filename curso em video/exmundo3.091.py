# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

# Import the randint function to generate random numbers from 1 to 6.
from random import randint
# Import tha sleep function to generate time. 
from time import sleep

# creates a dictionary with the players and their dice roll results
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6),}

# Displays the results that each player rolled on the dice.
print('Valores sorteados:')


for k, v in jogo.items():
    # displays the player and the results.
    sleep(0.5)
    print(f'{k} tirou {v} no dado.')
    
#Create an empty list that will store the players for tho ranking.
ranking = []

# Add the data from the dictionary to the list as tuples.( player, value)
for jogador, valor in jogo.items():
    ranking.append((jogador, valor)) # Add a tupla to the lista.
    
# define a function that returns the dice value( position 1 of the tuple)
def pegar_valor(tupla):
    return tupla[1] # return only the dice value

# Sort the list of tuples, from highest to lowest value.
ranking.sort(key=pegar_valor, reverse=True)
print()
print('-=' * 30)

# Displays the final ranking with the player's positions
print('\nRanking dos jogadores: ')
for i,(jogador , valor) in enumerate(ranking, start=1):
    sleep(0.5)
    print(f'{i}º lugar: {jogador} com {valor}') # Show position, player and value.
