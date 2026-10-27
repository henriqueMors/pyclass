import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('bd/meubanco.db')
cursor = conexao.cursor()

# 2 - Exclusão de dados
id_filme = 16
cursor.execute(
    "DELETE FROM filmes WHERE id = ?",
    (id_filme,)
)

conexao.commit()

print("Dados excluídos com sucesso")