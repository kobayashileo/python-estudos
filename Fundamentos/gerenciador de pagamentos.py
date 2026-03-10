
try:
    print('========== PAGAMENTO ==========')
    valor = float(input("Preço das compras: R$"))
    print("FORMAS DE PAGAMENTO")
    print("[ 1 ] - À vista dinheiro / cheque")
    print("[ 2 ] - À vista cartão")
    print("[ 3 ] - 2x no cartão ")
    print("[ 4 ] - 3x ou mais no cartão ")

    opcao = int(input("Selecione a sua opção: "))
    if opcao == 1:
        vd = valor - (valor * 0.1)
        print("Sua compra de R${:.2f} sairá por R${:.2f}!".format(valor, vd))
    elif opcao == 2:
        vd = valor - (valor * 0.05)
        print("Sua compra de R${:.2f} sairá por R${:.2f}!".format(valor, vd))
    elif opcao == 3:
        parcela = valor / 2
        print("Sua compra de R${:.2f} será paga em 2 parcelas de R${:.2f}!".format(valor, parcela))
    elif opcao == 4:
        parcela = int(input("Digite em quantas vezes você quer parcelar: "))
        vtj = valor * 1.2
        vtpj = vtj / parcela
        print("Como você irá parcelar em 3 vezes ou mais, sua compra terá juros de 20%!")
        print("Portanto, sua compra de R${:.2f} ficará em R${:.2f}, \n e parcelado em {} vezes cada parcela ficará no valor de R${:.2f}"
        .format(valor, vtj, parcela, vtpj))
    else:
        print("OPÇÃO INVÁLIDA!!")
except ValueError:
    print("Digite um valor válido!!")