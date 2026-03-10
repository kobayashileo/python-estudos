numero = int(input("Digite um número: "))
cd = 0
ld = []
for i in range(1, numero + 1):
    print(i, end =  ' ')
    if numero % i == 0:
        cd += 1
print(f"\nEsse número foi divisivel {cd} vezes!") 
if cd == 2:
    print(f"Portanto, o número {numero} É PRIMO!!")
else: 
    print(f"Portanto, o número {numero} NÃO É PRIMO!!")