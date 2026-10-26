import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('bd/meubanco.db')
cursor = conexao.cursor()

# 2 - Leitura de Dados
dados = cursor.execute("SELECT * FROM filmes WHERE nota >= 9")

print(dados.fetchall())