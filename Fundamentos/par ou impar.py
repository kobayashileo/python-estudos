import random
rodando = True

print("=======" * 4)
print("PAR OU ÍMPAR")
print("=======" * 4)

while rodando:
    j = int(input("Digite o número que quer jogar: "))
    ej = str(input("Par ou ímpar? [P/I] ")).upper()
    pc = random.randint(1, 10)
    soma = j + pc

    par = False
    impar = False

    if (j + pc) % 2 == 0:
        par = True
    else:
        impar = True

    print("Você escolheu {}, o computador escolheu {}, e {} + {} = {}, então..."
        .format(j, pc, j, pc, soma))

    if ej == "P" and par == True:
        print("Parabéns, você ganhou do computador!!")
    elif ej == "I" and impar == True:
        print("Parabéns, você ganhou do computador!!")
    else:
        print("Que pena! O computador ganhou!!")

    opcao = str(input("Deseja jogar de novo? [S/N] ")).upper()

    if opcao == "N":
        print("Volte sempre!")
        rodando = False