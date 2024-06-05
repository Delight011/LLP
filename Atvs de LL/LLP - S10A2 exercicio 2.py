# Palavra secreta
palavra_secreta = "python"

# Lista para armazenar as letras já adivinhadas
letras_adivinhadas = []

# Número máximo de tentativas permitidas
max_tentativas = 3

# Contador de tentativas
tentativas = 0

# Loop principal do jogo
while True:
    # Mostra a palavra com as letras já adivinhadas
    palavra_mostrada = ""
    for letra in palavra_secreta:
        if letra in letras_adivinhadas:
            palavra_mostrada += letra
        else:
            palavra_mostrada += "_ "
    print("Palavra: ", palavra_mostrada)

    # Solicita ao usuário uma letra
    letra = input("Digite uma letra: ")

    # Verifica se a letra já foi adivinhada antes
    if letra in letras_adivinhadas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    # Adiciona a letra às letras já adivinhadas
    letras_adivinhadas.append(letra)

    # Verifica se a letra está na palavra secreta
    if letra in palavra_secreta:
        print("Correto!")
    else:
        print("Incorreto!")
        tentativas += 1

    # Verifica se o usuário adivinhou todas as letras ou atingiu o limite de tentativas
    if all(letra in letras_adivinhadas for letra in palavra_secreta):
        print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
        break
    elif tentativas == max_tentativas:
        print("Você errou {} vezes. A palavra secreta era: {}".format(max_tentativas, palavra_secreta))
        break