while True:
    try:
        altura = float(input("Digite sua altura entre 1 a 3 metros: "))

        if 0 <= altura <= 3:
            break
        else:
            print("A altura deve estar entre 1 ou 3 metros. ")
    except ValueError:
        print("Digite um valor válido")

print("Sua altura é", altura)         