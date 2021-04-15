import sqlite3


class AgendaDB:
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    def insert(self, name, phone):
        query = 'INSERT OR IGNORE INTO agenda(name, phone) VALUES(?, ?)'
        self.cursor.execute(query, (name, phone))
        self.conn.commit()

    def update(self, name, phone, ident):
        query = 'UPDATE OR IGNORE agenda SET name=?, phone=? WHERE id=?'
        self.cursor.execute(query, (name, phone, ident))
        self.conn.commit()

    def delete(self, ident):
        query = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(query, (ident,))
        self.conn.commit()

    def read(self):
        query = 'SELECT * FROM agenda'
        self.cursor.execute(query)

        for line in self.cursor.fetchall():
            print(line)

    def search(self, attr, value):
        query = 'SELECT * FROM agenda WHERE ' + attr + ' LIKE ?'
        self.cursor.execute(query, (f'%{value}%',))

        for line in self.cursor.fetchall():
            print(line)

    def close_conn(self):
        self.conn.close()
        self.cursor.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    # agenda.insert('Emma Watson', '141522')
    # agenda.insert('Fernanda', '151621')
    # agenda.insert('Daniel', '111220')
    # agenda.insert('John', '192033')
    # agenda.insert('Rose', '181729')
    # agenda.insert('Andrew', '232239')

    # agenda.insert('Luiz Otávio', '212233')
    # agenda.insert('Luiz Felipe', '212234')
    # agenda.insert('Ronaldo Luiz', '212235')

    # agenda.insert('Luiza', '212236')

    # agenda.update('John Cooper', '192032', 7)
    # agenda.delete(8)
    agenda.read()

    print('#' * 20)
    agenda.search('name', 'Luiz')

    print('#' * 20)
    agenda.search('phone', '212233')



