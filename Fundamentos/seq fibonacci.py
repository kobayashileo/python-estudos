print("=====" * 4)
print("Sequência de Fibonacci")
print("=====" * 4)
termos = int(input("Quantos termos você quer mostrar? ")) - 1
qtd_t = 0
t1 = 0
t2 = 1
t3 = 0

while qtd_t <= termos:
    if qtd_t == 0:
        qtd_t += 1
        print(f"{t1}", end = " -> ")
        print(f"{t2}", end = " -> ")
    else:   #  0   1   1
        qtd_t += 1
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        print(f"{t3}", end = " -> ")
print("Acabou!")