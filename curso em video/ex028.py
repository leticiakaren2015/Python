# Escreva um programa que faça o computador “pensar”
# em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5)  # Faz  computador "PENSAR"

print('Vou penssar em um número entre 0 e 5. Trente adivinhar...')
jogador = int(input('Em que número eu pensei? '))  # Jogador tente adivinhar

print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('PARABÉNS! você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e nã no {}!'.format(computador, jogador))
