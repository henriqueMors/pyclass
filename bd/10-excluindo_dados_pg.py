from conexao_post import conn

cursor_obj = conectar()

sql = """
    DELETE FROM games
    WHERE id = %s
"""

cursor_obj.execute(sql, (5, ))

conn.commit()

print("Dados excluídos com sucesso")

conn.close()