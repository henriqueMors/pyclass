import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('bd/meubanco.db')
cursor = conexao.cursor()

# 2 - Atulizando dados
id = 2
cursor.execute(
    """
        UPDATE filmes SET nota = ?
        WHERE id = ?
    """,
    (8.5, id)
    
)

conexao.commit()

print("Dados atualizados")