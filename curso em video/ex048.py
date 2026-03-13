#  Faça um programa que calcule a soma entre todos os números que
#  são múltiplos de três e que se encontram no intervalo de 1 até 500.

cont = 0  # contador
soma = 0  # acumulaodor

for n in range(1, 501, 2):
    if n % 3 == 0:
        cont = cont + 1  # estou acumulando número, também poderia substituir por ( cont += 1 )
        soma = soma + n  # estou somanto todos os n que são divisivel por três, tbm poderia substituir por (soma += n)
print("A soma entre todos os {} valores solicitados é {}".format(cont, soma))
