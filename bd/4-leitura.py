import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Leitura de Dados
dados = cursor.execute("SELECT * FROM filmes")

print(dados.fetchall())