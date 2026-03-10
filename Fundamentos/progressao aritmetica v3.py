try:
    print("=" * 20)
    print("10 TERMOS DE UMA PA")
    print("=" * 20)

    pmt = int(input("Digite o primeiro termo: "))
    r = int(input("Digite a razão: "))

    termo = pmt
    cont = 1
    total_termos = 10

    while cont <= total_termos:
        print(f"{termo}", end=" -> ")
        termo += r
        cont += 1

        if cont > total_termos:
            qtd_t = int(input("\nQuantos termos mais deseja mostrar? "))
            total_termos += qtd_t

            if qtd_t == 0:
                print(f"Progressão finalizada com {total_termos} termos mostrados")

    print("ACABOU!")

except ValueError:
    print("Digite um valor válido!!!")