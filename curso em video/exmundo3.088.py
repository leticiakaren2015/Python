# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

import random
from time import sleep

print( '-=' * 30)
print(f"{'PALPITE DA MEGA SENA':^60}")
print( '-=' * 30)

# Início de uma laço infinito (usado para repetir em caso de erro)
# Start of an infinite loop (used to retry in case of error)
while True:
    
    # Solicitar ao usuário a quantidade de jogos e converter para inteiro. 
    # Asks the user how many games to generate and converts input to integer.
    try:
        quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
        print()
        print('GERANDO JOGOS...')
        
        # Exibir mensagem e aguarda 1 segundo (efeito visual)
        # Shows a message and waits 1 second (visual effect)
        sleep(1)
        
        # Cria uma lista para armazenar todo os jogos.
        # Creates a list for store all the games.
        jogos = list()
        
        for i in range(quantidade):
            # Sorteia 6 números únicos entre 1 e 60, e depois classificar em ordem crescente
            # Draws 6 unique numbers from 1 to 60, and sorts them in ascending order.
            jogo = sorted(random.sample(range(1, 61), 6))
            
            # Adicionar o jogo sorteado a lista de jogos.
            # Adds the  drawn games to the list of games.
            jogos.append(jogo)
            
            # Exibir o jogo atual numerado.
            # Displays the current games with numbering
            print(f'Jogo {i + 1}: {jogo}')
            
            # Pausa de 1 segundo antes de gerar o proximo jogo.
            # 1-second pause before generating the next game. 
            sleep(1)
    
        # Imprime  uma linha de separação e a mensagem centralizada.
        # prints a separating line and a centered message.
        print('-' * 60)
        print(f"{'Boa sorte!':^60}")
        
    except ValueError:
        # Trata erro caso o usuario digite algo que nao seja numero.
        # handles error in case user inputs something that isn't a number.
        print('Entrada Inválida! Certifique-se um número válido.')
    
    # Sai do laco( isso faz o loop rodar apena s uma vez, a menos que de erro).
    # Exits tho loop (this makes the loop run only once, unless there's an error).    
    break
