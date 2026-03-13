r1 = float(input("Primeiro seguimento. "))
r2 = float(input("Segundo seguimento. "))
r3 = float(input("Terceiro seguimento. "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos acima PODEM FORMAR um triângulo ", end="")
    if r1 == r2 == r3:
        print("\033[33mEQUILÁTERO.\033[m")
    elif r1 != r2 != r3 != r1:
        print("\033[36mESCALENO.\033[m")
    else:
        print("\033[35mISOSCELES.\033[m")
else:
    print("Os seguimento acima \033[31mNÃO PODEM FORMAR\033[m um Triângulo!")
