while True:
    try:
        valor = float(input("Digite um valor de saque até 1000: "))

        if 0 <= valor <= 1000:
            break
        else:
            print("o valor deve estar entre 0 e 1000.")
    except ValueError:
        print("Digite um número válido")

print("saque registrado! ", valor)