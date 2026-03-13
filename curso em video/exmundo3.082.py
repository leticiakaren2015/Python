# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão 
# conter apenas os valores pares e os valores ímpares digitados, 
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.


# Criando a primeira lista com números digitados pelo usuário
lista = []
while True:
    try:
        numero = int(input('Digite um número ( ou pressione Enter para sair): '))
        lista.append(numero)
        
    except ValueError:  # Se o usuário não digitar um número, o loop para
        break 

# Criando a segunda lista apenas com os números pares
# Utilizando a Forma com List Comprehension
lista_pares = [num for num in lista if num % 2 == 0] 

# Criando a segunda lista apenas com os números ímpares
# Utilizando a Forma tradicional ( Usando for) 
lista_impar = []
for num in lista:
    if num % 2 != 0:
        lista_impar.append(num)

# Exibindo as listas
print(f'Primeira lista {lista}')
print (f'Segunda lista, apenas os números pares{lista_pares}')
print(f'Terceira lista, apenas os números ímpares {lista_impar}')
