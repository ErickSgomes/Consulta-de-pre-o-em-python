produtos = {
    "banana": 3.50,
    "maçã": 2.99,
    "laranja": 1.99
}

produto_pesquisado = input("Digite o nome do produto: ")

if produto_pesquisado in produtos:
    preco = produtos[produto_pesquisado]
    print(f"O preço da {produto_pesquisado} é R${preco:.2f}")
else:
    print("Produto não encontrado.")
