import sqlite3

conn = sqlite3.connect('oficina.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        endereco TEXT,
        telefone TEXT,
        email TEXT,
        cep TEXT,
        cidade TEXT,
        estado TEXT,
        moto TEXT,
        problema TEXT
    )
''')

conn.commit()
conn.close()

print("Banco de dados atualizado com sucesso!")
