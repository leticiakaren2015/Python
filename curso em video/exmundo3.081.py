# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre: 
# A) Quantos números foram digitados. 
# B) A lista de valores, ordenada de forma decrescente. 
# C) Se o valor 5 foi digitado e está ou não na lista.


valores = []
while True:
    
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta in 'N':
        break
    
print(f'Os números digitados foram {valores}')
valores.sort(reverse=True)
print(f'Os números digitados em ordem decrescente são {valores}')

if 5 in valores:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista.')