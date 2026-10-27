from conexao_post import conectar

cursor_obj = conectar()

cursor_obj.execute("SELECT * FROM games")

result = cursor_obj.fetchall()

print(result)