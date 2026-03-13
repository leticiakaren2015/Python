# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.



player = dict() # Creating a dictionary | # Criando um dicionario chamado JOGADOR
matches = list() # Creating a list | # Criando uma lista chamada PARTIDAS
player['name'] = str(input('name of player: ')) # Asks for the player name. | # Pedir o nome dod jogador.
total = int(input(f'how many matches {player["name"]} it played? ')) # Asks for  how many matches the player it played. | # Perguntar quantas partidas o jogador jogou.
for c in range(0 , total):
    matches.append(int(input(f'   How many goals in the match {c + 1}? '))) # Store how many goals in the match | # Armazenar quantos gols na partida.
player['goals'] = matches[:] # key goals receive a copy of matches | # Chave gols recebe uma copia de PARTIDAS
player['total'] = sum(matches) # key total receive the matches sum | # Chave total recebe a soma das partidas
print('-=' * 30)
print(player)
print('-=' * 30)
for k, v in player.items(): # Para cada key, value em jogador.items():
    print(f'the field {k} has the value {v}') # O campo {k} tem o valor {v}
