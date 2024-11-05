produtos = []

def adicionar_produto(nome, preco):
    produto = {"nome": nome, "preco": preco}
    produtos.append(produto)
    print(f"Produto {nome} adicionado com sucesso!")

def remover_produto(nome):
    for i, produto in enumerate(produtos):
        if produto['nome'] == nome:
            del produtos[i]
            print(f"Produto {nome} removido com sucesso!")
            return
    print(f"Produto {nome} não encontrado.")

def consultar_produto(nome):
    for produto in produtos:
        if produto['nome'] == nome:
            print(f"O preço de {produto['nome']} é R${produto['preco']}")
            return
    print(f"Produto {nome} não encontrado.")

# Exemplo de uso
adicionar_produto("Banana", 2.5)
adicionar_produto("Maçã", 3.0)

consultar_produto("Banana")
remover_produto("Maçã")
