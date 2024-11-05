produtos = [
    {"nome": "Banana", "preco": 2.5, "codigo": "FRU001"},
    {"nome": "Maçã", "preco": 3.0, "codigo": "FRU002"},
    {"nome": "Laranja", "preco": 2.0, "codigo": "FRU003"}
]

def consultar_produto(nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            return produto
    return None

while True:
    nome_produto = input("Digite o nome do produto que deseja buscar (ou 'sair' para encerrar): ")
    if nome_produto.lower() == "sair":
        break
    produto = consultar_produto(nome_produto)
    if produto:
        print(f"O preço da {produto['nome']} é R${produto['preco']:.2f}")
    else:
        print("Produto não encontrado.")