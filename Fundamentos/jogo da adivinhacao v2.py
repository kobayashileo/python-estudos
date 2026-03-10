
import random

print("============ JOGO DA ADIVINHAÇÃO ============")
print("Olá! Acabei de pensar em um número entre 0 e 10")
print("Será que você consegue adivinhar qual número eu pensei?")

pc = random.randint(0, 10)

acertou = False
cont = 0

while not acertou:
    jogador = int(input("Digite um número: "))
    cont += 1
    if jogador == pc:
        print(f"Parabéns, você acertou com {cont} jogadas!!!")
        acertou = True
    elif jogador < pc:
        print("Mais... Tente mais uma vez!")
    else:
        print("Menos... Tente mais uma vez!")