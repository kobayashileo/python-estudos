
rodando = True
soma = 0
cont_num = 0 

print("Caso queira parar, basta digitar 999!")
while rodando:
    numero = int(input("Digite um número: "))
    if numero != 999:
        cont_num += 1
        soma += numero
    else:
        print(f"Você digitou {cont_num} números e a soma entre eles é igual a {soma}!")
        rodando = False