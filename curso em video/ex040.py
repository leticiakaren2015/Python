# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))
media = (nota1 + nota2) / 2

if media <= 7:
    print("Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}".format(nota1, nota2, media))
    print("O aluno está \033[31mREPROVADO\033[m")

elif 7 > media >= 5:
    print("Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}".format(nota1, nota2, media))
    print("O aluno está em \033[33mRECUPERAÇÃO\033[m")

else:
    print("Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}".format(nota1, nota2, media))
    print("O aluno está \033[34mAPROVADO\033[m")
