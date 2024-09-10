
Nota_1 = input("Primeira nota: ")
Nota_2 = input("Segunda nota: ")
Nota_3 = input("Terceira nota: ")
Nota_4 = input("Quarta nota: ")

Nota_1 = float(Nota_1)
Nota_2 = float(Nota_2)
Nota_3 = float(Nota_3)
Nota_4 = float(Nota_4)

media = (Nota_1 + Nota_2 + Nota_3 + Nota_4)/4

if media >= 6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print(f"Sua média é {media}, você está {situacao}.")
    
