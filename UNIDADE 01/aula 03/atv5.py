# mensagens de boas-vindas
print("Bem-vindo a classificação de filmes!")
print("Você tem cinco filmes para classificar.")
print("Digite '0' a qualquer momento para parar.\n")

filmes = ["Filme 1", "Filme 2", "Filme 3", "Filme 4"]

for filme in filmes:
    #solicita a classificação ao usuario
    classificacao = input(f"Como você classificaria '{filme}' de 1 a 5? (Ou 0 para parar): ")

    # verifica se o usuario deseja parar digitando 0
    if classificacao == '0':
        print("Que pena que você não irá classificar mais os filmes.")
        break
    
    # valida a classificação fornecida pelo usuario
    classificacao = int(classificacao)
    
    # usuario só pode fornecer nota de 1 a 5
    if classificacao < 1 or classificacao> 5:
        print("Por favor, digite um número entre 1 e 5.")
    else:
        print(f"Obrigado por classificar '{filme}' com {classificacao} estrelas!\n")
    
print("Obrigado por classificar todos os filmes!")