#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrá-lo por extenso.


cont = ('zero', 'um', 'dois', 'três','quatro','cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
        'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    
    while True:
        número = int(input('Digite um número entre 0 e 20: '))
        if  0 <= número <= 20:
            break
        print('Tente novamente. ', end='')
        
    print(f'Você digitou o número {cont[número]}')   
        
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    
print('Programa encerrado! ')
