# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está 
# com os parênteses abertos e fechados na ordem correta.

# Solicitar a expressão ao usuário
expressão = input('Digite uma expressão: ')

# Criar uma pilha vazia para armazenar os parênteses abertos
pilha = []

# Percorrer cada caractere da expressão
for simbolo in expressão:
    if simbolo == '(':
        # Se o caractere for um parêntese aberto, adicionar na pilha
        pilha.append(simbolo)
    elif simbolo == ')':
        # Se o caractere for um parêntese fechado:
        if pilha:
            # Se a pilha não estiver vazia, retirar o último parêntese aberto
            pilha.pop()
        else:
            # Se a pilha estiver vazia, não há parêntese para fechar - expressão errada.
            pilha.append(simbolo)   # Aqui, adicionamos para marcar o erro
            break  # E saímos do loop, pois a expressão já esta errada
        
        
# Após percorrermos toda a expressão, se a pilha estiver vazia, todos os parêntese foram 
# fechados corretamente.


if not pilha:
    print('Sua expressão está CORRETA!')
else:
    print('Sua expressão está ERRADA!')

