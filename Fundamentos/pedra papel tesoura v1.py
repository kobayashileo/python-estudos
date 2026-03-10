import random

print ("-=-" * 13)
print("Bem vindo ao Pedra, Papel e Tesoura!")
print ("-=-" * 13)
opcoes = ["Pedra", "Papel", "Tesoura"]
print("Para jogar, selecione uma das opções: ")
for i, opcao in enumerate(opcoes):
    print(f"[ {i + 1} ] - {opcoes[i]}")

oj = opcoes[int(input("Selecione a sua opção: ")) - 1]
pc = random.choice(opcoes)

print(f"O jogador escolheu {oj}!")
print(f"O computador escolheu {pc}!")

if oj == pc:
    print("Empatouu!!!")
elif oj == "Pedra" and pc == "Papel":
    print("O Pc Ganhou!!!")
elif oj == "Pedra" and pc == "Tesoura":
    print("Parabéns!! Você Ganhou!!!")
elif oj == "Tesoura" and pc == "Pedra":
    print("O Pc Ganhou!!!")
elif oj == "Tesoura" and pc == "Papel":
    print("Parabéns!! Você Ganhou!!!")
elif oj == "Papel" and pc == "Tesoura":
    print("O Pc Ganhou!!!")
elif oj == "Papel" and pc == "Pedra":
    print("Parabéns!! Você Ganhou!!!")