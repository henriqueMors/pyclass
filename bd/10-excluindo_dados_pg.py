from conexao_post import conectar

cursor_obj = conectar()

sql = """
    DELETE FROM games
    WHERE id = %s
"""

cursor_obj.execute(sql, (5, ))

conectar.commit()

print("Dados excluídos com sucesso")

conectar.close()