# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER


from datetime import date


nome_do_atleta = str(input("Digite o seu nome: ")).strip().lower()
ano_de_nascimento = int(input("Digite o seu ano de nascimento: "))
atual = date.today().year
idade = atual - ano_de_nascimento

if idade <= 9:
    categoria = "MIRIM"
    print("Sua categoria é MIRIM.")

elif idade <= 14:
    categoria = "INFANTIL"
    print("Olá {}! Sua idade é {} anos. Então você pertence a categoria é INFANTIL".format(nome_do_atleta, idade))

elif idade <= 19:
    categoria = "JÚNIOR"
    print("""Olá {}! Sua idade é {} anos. Então você pertence 
    a categoria é \033[31mJÚNIOR\033[m.""".format(nome_do_atleta, idade))

elif idade <= 25:
    categoria = "SÊNIOR"
    print("""Olá {}! Sua idade é {} anos. Então você pertence 
    a categoria é \033[35mSÊNIOR\033[m.""".format(nome_do_atleta, idade))

else:
    categoria = "MASTER"
    print("""Olá {}! Sua idade é {} anos. Então você pertence 
    a categoria é \033[34mMASTER\033[m.""".format(nome_do_atleta, idade))
