# repetição while, não sabemos onde parar

numero = int(input("Digite um número ou digite 0 para sair: "))

while numero != 0:
    if numero % 2 == 0:
        print("O número é par")
    else: 
        print("O número é impar")
    numero = int(input("Digite um número ou digite 0 para sair: "))


