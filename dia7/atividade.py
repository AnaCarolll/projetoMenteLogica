# #adivinhe um numero

# import random
# print("Bem vindo ao jogo de adivinhar o número!")

# while True:

#     numeroSecreto = random.randint(1, 10)

#     print(numeroSecreto)

#     tentativas = 3
#     print("Você tem 3 tentativas para adivinhar o número entre 1 e 10.")
#     while tentativas > 0:
#         palpite = int(input("Digite seu palpite: "))

#         if palpite == numeroSecreto:
#             print("Parabéns! Você adivinhou o número!")
#             break
#         else:
#             tentativas -= 1
#             print(f"Errado! Você tem {tentativas} tentativas restantes.")

#     break



while True:
    numerSecreto = 2
    tentativas = 4

    print("Você tem 4 tentativas para adivinhar o número entre 1 e 10.")
    while tentativas > 0:
        palpite = int(input("Digite seu palpite: "))

        if palpite == numerSecreto:
            print("Parabéns! Você adivinhou o número!")
            break
        else:
            tentativas -=1
            print(f"Errado! Você tem {tentativas} tentativas restantes.")
    break
