from conexao_post import conectar

conn = conectar()
cursor_obj = conn.cursor()

sql = """
    UPDATE games
    SET NAME = %s
    WHERE ID = %s
"""

cursor_obj.execute(sql, ("Fifa 23", 3))
conectar.commit()
print("Dados atualizados com sucesso")
conectar.close()
