import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Atulizando dados
id = 1
cursor.execute(
    """
        UPDATE filmes SET nota = ?
        WHERE id = ?
    """,
    (8.5, id)
    
)

conexao.commit()

print("Dados atualizados")