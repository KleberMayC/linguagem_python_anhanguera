for numero in range(3,11):
    if numero % 2 == 0:
        print("O primeiro número encontrado par é:", numero)
        break
    
for numero in range(1,11):
    if numero == 5: #aqui ira pular o 5
        continue
    print(numero)
