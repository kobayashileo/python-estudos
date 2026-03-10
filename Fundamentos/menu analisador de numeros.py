import time

sair = False

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o primeiro valor: "))
while not sair:
    print("============ MENU DE OPERAÇÕES MATEMÁTICAS SIMPLES ============")
    print("[ 1 ] - Somar")
    print("[ 2 ] - Multiplicar")
    print("[ 3 ] - Maior")
    print("[ 4 ] - Novos números")
    print("[ 5 ] - Sair")
    opcao = int(input("Selecione uma opção: "))

    if opcao == 1:
        print("Carregando...")
        time.sleep(2)
        print(f"{n1} + {n2} é igual a {n1 + n2}!")
    elif opcao == 2:
        print("Carregando...")
        time.sleep(2)
        print(f"{n1} x {n2} é igual a {n1 * n2}!")
    elif opcao == 3:
        print("Carregando...")
        time.sleep(2)
        if n1 > n2:
            print(f"O maior número é o {n1}!")
        else:
            print(f"O maior número é o {n2}!")
    elif opcao == 4:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o primeiro valor: "))
    elif opcao == 5:
        print("Volte sempre!")
        sair = True
    else:
        print("Selecione uma opção válida!!!")