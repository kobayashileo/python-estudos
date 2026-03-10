rodando = True

print("=======" * 4)
print("Bem vindo à tabuada digital!")
print("=======" * 4)

while rodando:
    numero = int(input("Quer ver a tabuada de qual valor? "))
    print("------" * 6)
    for i in range(10):
        print(f"{numero} x {i + 1} = {numero * (i + 1)}")
        i +=1
    print("------" * 6)
    opcao = input("Deseja ver de outro valor? [S/N] ").upper()
    if opcao != 'S':
        print("Volte sempre!")
        rodando = False