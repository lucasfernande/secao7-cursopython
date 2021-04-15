import sqlite3

conn = sqlite3.connect('basedados.db')  # objeto de conexão
cursor = conn.cursor()  # objeto de cursor

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes('  # criando uma tabela
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')

"""
cursor.execute('INSERT INTO clientes(nome, peso) VALUES("Luiz", 76.9)')  # inserindo um valor na tabela
cursor.execute('INSERT INTO clientes(nome, peso) VALUES(?, ?)', ('Maria', 52.5))  # desta forma, previne o sql injection
cursor.execute(
    'INSERT INTO clientes(nome, peso) VALUES(:nome, :peso)',
    {'nome': 'Otávio', 'peso': 81.5}
)  # outra forma de previnir o sql injection

cursor.execute(
    'INSERT INTO clientes VALUES(:id, :nome, :peso)',
    {'id': None, 'nome': 'Joãozinho', 'peso': 30.1}
)  # outra forma

conn.commit()  # executa os comandos acima
"""

# cursor.execute(
#     'UPDATE clientes SET peso=:peso WHERE id=:id',
#     {'peso': 49.4, 'id': 2}
# )  # atualizando o peso do id 2

cursor.execute('DELETE FROM clientes WHERE id=:id', {'id': 4})  # deletando um registro da base
conn.commit()

cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    ident, nome, peso = linha
    print(f'ID: {ident}, NOME: {nome}, PESO: {peso}')

cursor.close()  # fechando o cursor
conn.close()  # fechando a conexão
