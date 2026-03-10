
frase = input("Digite uma frase: ").strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1 , -1):
    inverso += junto[letra]

if junto == inverso:
    print(f'A frase "{frase}" ao contrário é:')
    print(inverso)
    print("Portanto, essa frase É um palíndromo!!")
else: 
    print(f"A frase {junto} ao contrário é:")
    print(inverso)
    print("Portanto, essa frase NÃO É um palíndromo!!")