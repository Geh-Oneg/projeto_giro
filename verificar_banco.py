import sqlite3

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

try:
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    if clientes:
        for cliente in clientes:
            print(cliente)
    else:
        print("Nenhum cliente cadastrado.")
except sqlite3.OperationalError as e:
    print("Erro:", e)

conn.close()

