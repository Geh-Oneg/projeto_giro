import sqlite3

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ordens_servico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    nome_oficina TEXT,
    cnpj TEXT,
    endereco_oficina TEXT,
    telefone_oficina TEXT,

    nome_cliente TEXT,
    telefone_cliente TEXT,
    endereco_cliente TEXT,
    email_cliente TEXT,

    marca TEXT,
    modelo TEXT,
    ano TEXT,
    cor TEXT,
    placa TEXT,
    quilometragem TEXT,
    chassi TEXT,

    problema TEXT,
    servicos_pecas TEXT,
    mao_obra TEXT,
    total TEXT,
    forma_pagamento TEXT,
    garantia TEXT,

    data_entrada TEXT,
    data_prevista TEXT,
    status TEXT,
    observacoes TEXT
)
""")

conn.commit()
conn.close()

print("Tabela 'ordens_servico' criada com sucesso.")

