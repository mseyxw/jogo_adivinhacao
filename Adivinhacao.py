import random

pontos = 1000
tentativas = 5

print ("********************")
print ("JOGO DE ADIVINHAÇÃO!")
print ("********************")

print("(1) FÁCIL \n(2) MÉDIO \n(3) DIFÍCIL",)
nivel = int(input("Escreva o número do nível que quer jogar: "))

if (nivel < 1 or nivel > 3):
    print("Escolha inválida!")

elif (nivel == 1):
    print("Você escolheu o nível FÁCIL!")
    num_secreto = int(random.randrange(1, 11))
    num_max = 10

elif (nivel == 2):
    print("Você escolheu o nível MÉDIO!")
    num_secreto = int(random.randrange(1, 26))
    num_max = 25

elif (nivel == 3):
    print("Você escolheu o nível DIFÍCIL!")
    num_secreto = int(random.randrange(1, 51))
    num_max = 50

for i in range(1, tentativas + 1):
    print("Tentativa {} / {}".format(i, tentativas))
    num_escolhido = int(input(f"Digite um número entre 1 e {num_max}: "))

    if (num_escolhido < 0 or num_escolhido > num_max):
        print(f"Você deve digitar um número entre 1 e {num_max}!")
        continue
    if (num_secreto == num_escolhido):
        print(f"Você acertou!")
        break
    else:
        if (num_secreto > num_escolhido):
            print("Você errou! O número secreto é maior.")
            pontos = pontos - (abs(num_secreto - num_escolhido))
        elif (num_secreto < num_escolhido):
            print("Você errou! O número secreto é menor.")
            pontos = pontos - (abs(num_secreto - num_escolhido))

print(f"O número secreto era {num_secreto}!")
print(f"TOTAL DE PONTOS = {pontos}")









