import random
import time

computador = random.randint(1,5)

print("Bem vindo ao jogo da adivinhação!")
print("Para jogar, basta tentar acetar o número escolhido entre 1 ao 5")
resposta = input("Qual número você acha que eu escolhi?? ")
print("Processando...")
time.sleep(3)

if resposta == computador:
    print("Parabéns, você acertou!")
else:
    print("Errou! O número certa era o {} !!!".format(computador))