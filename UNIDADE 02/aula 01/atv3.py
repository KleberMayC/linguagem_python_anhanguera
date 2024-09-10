linguagens = ["Python", "JavaScript", "Java", "C++", "Ruby", "Go"]

print("Antes da listcomp = ", linguagens)

linguagens = [item.lower() for item in linguagens] #lower é utlizado para deixar as letras minusculas
print("\nDepois da listcomp = ", linguagens)