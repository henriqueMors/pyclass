import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect('bd/meubanco.db')

# 2 - Criando o cursor
cursor = conexao.cursor()

# 3 - Criando a tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        ano INTEGER,
        nota REAL,
        UNIQUE(nome, ano)
    )
""")

# 4 - Fecha conexão
conexao.close()
print("Tabela foi criada")