# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


número = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))

print(f'Você digitou os números: {número}')
print(f'O número 9 apareceu {número.count(9)}')
if 3 in número:
    print(f' O número 3 apareceu na {número.index(3)+1}ª posição.')
else:
    print('O número 3 não foi digitado!')
print('Os números pares digitados foram ', end='')
for n in número:
    if n % 2 == 0:
        print(n, end=' ')