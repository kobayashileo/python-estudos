produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
estoque = [100, 150, 100, 120, 70, 180, 80]

produto = str(input("Digite o nome do produto: ")).lower()
print(produto)
if produto in produtos:
    i = produtos.index(produto)
    print(f'{produto.capitalize()}: {estoque[i]} em estoque')
else:
    print('Produto inválido! Por favor, digite um produto válido!!')