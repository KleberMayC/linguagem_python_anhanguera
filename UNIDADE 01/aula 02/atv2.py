idade = int(input("Digite sua idade: "))

# Operadores AND, OR, NOT
if idade < 18:
    print("Menor de idade")
elif idade >= 18 and idade < 65:
    print("Adulto")
else:
    print("Idoso")
