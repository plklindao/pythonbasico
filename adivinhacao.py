import random

print ("**********************")
print ("***jogo adivinhação***")
print ("**********************")

numero_secreto = random.randrange(1,101)
total_tentativas = 5
rodada = 1

while (rodada <= total_tentativas ):
    print("Tentativa {} de {}".format(rodada, total_tentativas))


    chute_str = input("Digite o seu numero: ")
    chute = int(chute_str)

    if(chute <1 or chute > 100):
        print("O número deve ser entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou")
        break
    else:
        if(maior):
            print("Diminui")
        elif(menor):
            print("Aumenta")
    rodada = rodada +1

print(numero_secreto)
print("fim de jogo!")