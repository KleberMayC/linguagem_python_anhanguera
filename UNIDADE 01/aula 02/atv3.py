idade = int(input("Por favor, digite sua idade"))

if idade < 12:
    print("Recomendamos o filme infantil FILME 1")
elif 12 <= idade <18:
    print("Recomendamos o filme para adolescentes FILME 2")
else:
    print("Recomendamos o filme para adultos FILME 3")
    
qtd_ingressos = 10

if qtd_ingressos > 0:
    print("Ingressos estão disponiveis")
else:
    print("Todos os ingressos estão esgotados")