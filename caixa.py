while True:
    try:
        valor = float(input("Digite um valor "))

        if 0 <= valor <= 1000:
            break
        else:
            print("o valor deve estar entre 0 e 1000.")
    except ValueError:
        print("Valor inválido")

print("Seu saque foi de ", valor)