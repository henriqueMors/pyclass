import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('bd/meubanco.db')
cursor = conexao.cursor()

# 2 - Exclusão de dados
id = (15, 14)
cursor.execute(
    """
        DELETE FROM filmes
        WHERE ID in (?, ?)
    """,
    id
)

conexao.commit()

print("Dados excluídos com sucesso")