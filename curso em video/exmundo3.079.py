# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, 
# em ordem crescente.

lista = list()

while True:
    
    numero = int(input('Digite um número: '))
    if numero in lista:
        print('Você já digitou esse numero não vou adicionar!')
    else:
        lista.append(numero)
        print('Adicionado com sucesso!')

    resposta = str(input('Quer continuar [S/N]: ')).strip().upper()
    if resposta != 'S':
        break
        
lista.sort()   
print (lista)