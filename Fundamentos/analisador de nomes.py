Nome = str(input("Digite seu nome completo: ")).strip()
print("Seu nome com letras maiúsculas é: {}".format(Nome.upper()))
print("Seu nome com letras maiúsculas é: {}".format(Nome.lower()))
print("Seu nome tem {} letras".format(len(Nome) - Nome.count(' ')))

separa = Nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))