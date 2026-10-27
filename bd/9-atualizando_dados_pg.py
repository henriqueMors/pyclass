from conexao_post import conectar

conn = conectar()
cursor_obj = conn.cursor()

sql = """
    UPDATE games
    SET NOME = %s
    WHERE ID = %s
"""

cursor_obj.execute(sql, ("Ghost Busters", 16))
conn.commit()
print("Dados atualizados com sucesso")
conn.close()