from conexao_post import conn

cursor_obj = conn.cursor()

games = [
    ('The Last of us II', 2020, 9.5),
    ('Spider Man 2', 2023, 10.0)
]

for game in games:
    cursor_obj.execute(
        """
            INSERT INTO games(name, year, score)
            VALUES (%s, %s, %s)
        """, game
        
    )
conn.commit()
print("Dados inseridos com sucesso!")
conn.close()