produtos = [
    {"nome": "Banana", "preco": 2.5, "codigo": "FRU001"},
    {"nome": "Maçã", "preco": 3.0, "codigo": "FRU002"},
    {"nome": "Laranja", "preco": 2.0, "codigo": "FRU003"}
]

def consultar_produto(nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            return produto
    return None  # Produto não encontrado

while True:
    print("\nMenu:")
    print("1. Consultar produto")
    print("2. Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nome_produto = input("Digite o nome do produto: ")
        produto_encontrado = consultar_produto(nome_produto)
        if produto_encontrado:
            print("Produto encontrado:")
            for chave, valor in produto_encontrado.items():
                print(f"{chave}: {valor}")
        else:
            print("Produto não encontrado.")
    elif opcao == "2":
        break
    else:
        print("Opção inválida.")