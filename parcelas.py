while True:
    try:
        parcelas = float(input("Digite o numero de parcelas: "))

        if 1 <= parcelas <= 12:
            break
        else:
            print("O número máximo de parcelas é de 12. ")
    except ValueError:
        print("Digite um número válido")

print("A quantidade de parcelas que vc pediu é de", parcelas)  