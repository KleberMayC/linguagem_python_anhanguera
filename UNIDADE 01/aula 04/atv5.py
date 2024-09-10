notas = [ 7.5, 4.0, 4.5, 8.5]

def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media
arredondar_media = lambda media: round(media, 2)

media = calcular_media(notas)
media_arredondada = arredondar_media(media)

situacao = "Aprovado" if media_arredondada >= 7 else "Reprovado"

print("Notas do estudante:", notas)
print("Média das notas:", media_arredondada)
print("Situação do estudante:", situacao)