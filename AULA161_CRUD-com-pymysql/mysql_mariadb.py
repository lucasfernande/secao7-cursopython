import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conectar():
    # conectando ao servidor
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conn
    finally:
        conn.close()


# with conectar() as conn:
#     with conn.cursor() as cursor:
#         query = 'INSERT INTO clientes(nome, sobrenome, idade, peso) VALUES(%s, %s, %s, %s)'
#         cursor.execute(query, ('Jack', 'Bauer', 64, 70))
#         conn.commit()

with conectar() as conn:
    with conn.cursor() as cursor:
        query = 'INSERT INTO clientes(nome, sobrenome, idade, peso) VALUES(%s, %s, %s, %s)'

        data = [
            ('Mariana', 'Figueiredo', 26, 55),
            ('Pedro', 'Henrique', 21, 68),
            ('Rose', 'Park', 25, 53)
        ]

        cursor.executemany(query, data)
        conn.commit()

with conectar() as conn:  # esse with fecha a conexão automaticamente
    with conn.cursor() as cursor:  # esse with fecha o cursor automaticamente
        cursor.execute('SELECT * FROM clientes')
        response = cursor.fetchall()

        for line in response:
            print(line)
