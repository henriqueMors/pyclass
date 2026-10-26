import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Exclusão de dados
id = (1, 2)
cursor.execute(
    """
        DELETE FROM filmes
        WHERE ID in (?, ?)
    """,
    id 
)

conexao.commit()

print("Dados excluídos com sucesso")