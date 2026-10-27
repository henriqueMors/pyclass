from conexao_post import conectar

conn = conectar()
cursor_obj = conn.cursor()

cursor_obj.execute("SELECT * FROM games")

result = cursor_obj.fetchall()

print(result)