from conexao_post import conectar

conn = conectar()
cursor_obj = conn.cursor()

sql = """
    DELETE FROM games
    WHERE id = %s
"""

cursor_obj.execute(sql, (16, ))

conn.commit()

print("Dados excluídos com sucesso")

conn.close()