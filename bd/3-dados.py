import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect('bd/meubanco.db')
cursor = conexao.cursor()

# 2 - Inserindo Dados
cursor.execute( 
    """
    INSERT OR IGNORE INTO filmes(nome, ano, nota)
    VALUES
        ('Tropa de Elite', 2007, 8.5),
        ('Cidade de Deus', 2002, 9.0),
        ('Central do Brasil', 1998, 8.0),
        ('O Auto da Compadecida', 2000, 9.0),
        ('Matrix', 1999, 8.7),
        ('O Poderoso Chefão', 1972, 9.2),
        ('Interestelar', 2014, 8.7),
        ('A Origem', 2010, 8.8),
        ('Toy Story', 1995, 8.3),
        ('Procurando Nemo', 2003, 8.1),
        ('Pantera Negra', 2018, 7.3),
        ('Divertida Mente', 2015, 8.1),
        ('Parasita', 2019, 8.5),
        ('Coringa', 2019, 8.4),
        ('Duna', 2021, 8.0)
    """
    
)
conexao.commit()
conexao.close()
print("Dados inseridos na tabela")