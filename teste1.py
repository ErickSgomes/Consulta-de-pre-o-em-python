import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()

# Criar a tabela (se não existir)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        preco REAL
    )
''')

def adicionar_produto(nome, preco):
    cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", (nome, preco))
    conn.commit()

def remover_produto(id):
    cursor.execute("DELETE FROM produtos WHERE id=?", (id,))
    conn.commit()

def consultar_produto(nome):
    cursor.execute("SELECT * FROM produtos WHERE nome=?", (nome,))
    resultado = cursor.fetchone()
    return resultado

# Exemplo de uso
adicionar_produto('Banana', 2.5)
adicionar_produto('Maçã', 3.0)

resultado = consultar_produto('Banana')
if resultado:
    print(f"O preço da {resultado[1]} é R${resultado[2]}")
else:
    print("Produto não encontrado")

# Fechar a conexão com o banco de dados
conn.close()