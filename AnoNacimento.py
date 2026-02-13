while True:
    try:
        nascimento = int(input("Digite que ano você nasceu: "))

        if 1900 <= nascimento <= 2026:
            break
        else:
            print("Seu ano de nascimento de estar entre 1900 e 2026. ")
    except ValueError:
        print("Digite um valor válido")

print("Sua data de nacimento é de", nascimento)