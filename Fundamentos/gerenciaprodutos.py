produtos = ['apple tv', 'macbook', 'iphone x', 'ipad', 'applewatch', 'airpods']

produto = str(input("Digite o nome do produto que quer substituir: ")).lower()

try:
    condicao = str(input('Tem certeza que deseja substituir o produto "{}"? Responda apenas sim ou não '.format(produto))).lower()
    if condicao == 'sim':
        produto_novo = str(input("Digite o nome do produto novo: ")).lower()
        i = produtos.index(produto)
        produtos[i] = produto_novo
        print(f'O "{produto}" foi substituido pelo "{produto_novo}" com sucesso!')
    else:
        print("Sem problemas, volte quando quiser!")
except ValueError:
    print('Produto que deseja substituir é inválido! Por favor, digite um produto válido!!')