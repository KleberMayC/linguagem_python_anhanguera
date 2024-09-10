def e_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = int(input("Insira um número: "))

if e_par(numero):
    print(f"{numero} é número par.")
else:
    print(f"{numero} é número ímpar.")