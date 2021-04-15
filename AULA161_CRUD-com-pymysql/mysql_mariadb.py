import pymysql.cursors

# conectando ao servidor
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='clientes',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with conn.cursor() as cursor:
    cursor.execute('SELECT * FROM clientes')
    response = cursor.fetchall()

    for line in response:
        print(line)


# fechando a conexão
conn.close()
