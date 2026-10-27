import psycopg2

def conectar():
    return psycopg2.connect(
        database='db_games',
        user='postgres',
        password='bd123456',
        host='localhost',
        port='5432'
    )