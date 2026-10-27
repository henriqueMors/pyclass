import pytest
import sqlite3

@pytest.fixture
def db_connection():
    """
    Fixture que configura uma conexão com um banco de dados SQLite
    temporário e garante a limpeza dos recursos após o teste
    """
    conn = sqlite3.connect(":memory:") # Cria BD em memória
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE users(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )             
    """
    )
    conn.commit()
    yield conn, cursor
    
    conn.close()
    
def test_database_insert(db_connection):
    """
    Testa a inserção de um usuário na tabela users do 
    BD SQlite
    """
    conn, cursor = db_connection
    cursor.execute("""
     INSERT INTO users (name, email) 
     VALUES (?, ?)              
    """, ("John Doe", "john.doe@example.com"))
    conn.commit()
    
    # Verificação da Inserção
    cursor.execute("SELECT * FROM users WHERE email = ?",
                   ("john.doe@example.com",))
    user = cursor.fetchone()
    assert user is not None
    assert user[1] == "John Doe"
    assert user[2] == "john.doe@example.com"
    
def test_database_no_duplicate_emails(db_connection):
    """
    Testa a inserção de usuários com e-mails duplicados.
    """
    conn, cursor = db_connection
    
    cursor.execute("""
     INSERT INTO users (name, email) 
     VALUES (?, ?)              
    """, ("Jane Smith", "jane.smith@example.com"))
    conn.commit()
    
    # Verificação de Tentativa para inserir e-mail duplicado
    with pytest.raises(sqlite3.IntegrityError):
        cursor.execute("""
        INSERT INTO users (name, email) 
        VALUES (?, ?)              
        """, ("Duplicate User", "jane.smith@example.com"))
        conn.commit()