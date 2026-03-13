# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.


núm = [[], []]
valor = 0

for c in range(1, 7):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)

núm[0].sort()
núm[1].sort()

print(f'Os valor pares digitados foram {núm[0]}')
print(f'Os valor ímpares digitados foram {núm[1]}')

