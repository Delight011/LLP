while True:
    senha = input("Crie uma senha: ")

    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue

    # Verifica se a senha contém números
    tem_numero = any(char.isdigit() for char in senha)
    if not tem_numero:
        print("A senha deve conter pelo menos um número.")
        continue

    # Verifica se a senha contém letras
    tem_letra = any(char.isalpha() for char in senha)
    if not tem_letra:
        print("A senha deve conter pelo menos uma letra.")
        continue

    # Se a senha atender a todos os critérios, saia do loop
    break

print("Senha criada com sucesso!")