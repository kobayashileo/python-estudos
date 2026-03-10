rodando = True
maior = 0
menor = 0
cont = 0
soma = 0 

while rodando: 
    numero = int(input("Digite um número: "))
    opcao = input("Deseja continuar? [S/N] ").upper()

    if opcao == 'S':
        if cont == 0:
            maior = numero
            menor = numero
            cont += 1
            soma += numero
        else:
            if numero > maior:
                maior = numero
                cont += 1
                soma += numero
            elif numero < menor:
                menor = numero
                cont += 1
                soma += numero
    else:
        if numero > maior:
                maior = numero
                cont += 1
                soma += numero
        elif numero < menor:
                menor = numero
                cont += 1
                soma += numero

        print(f"Você digitou {cont} números, e a média entre eles foi de {soma / cont}")
        print(f"O maior número foi o {maior}, e o menor foi o {menor}")

        rodando = False