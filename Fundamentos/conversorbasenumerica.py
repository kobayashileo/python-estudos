n = int(input("Digite um número inteiro: "))

print("Escolha uma das opções para conversão: ")
print("[ 1 ] - Converter para binário")
print("[ 2 ] - Converter para octal")
print("[ 3 ] - Converter para hexadecimal")

opção = int(input("Selecione a sua opção: "))  
if opção == 1:
    print("O número {} convertido para binário é: {}".format(n, bin(n)[2:]))
elif opção == 2:
    print("O número {} convertido para octal é: {}".format(n, oct(n)[2:]))
elif opção == 3:
    print("O número {} convertido para octal é: {}".format(n, hex(n)[2:]))
else: 
    print("Opção inválida!!")