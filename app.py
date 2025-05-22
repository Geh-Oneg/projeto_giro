from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Página inicial com ícones
@app.route('/')
def index():
    return render_template('index.html')

# Página com o menu de cadastros (clientes, motos, ordem)
@app.route('/cadastro')
def cadastro_menu():
    return render_template('cadastro.html')

# Formulário de cadastro de cliente
@app.route('/cadastro_cliente')
def cadastro_cliente():
    return render_template('cadastro_cliente.html')

# Rota que salva os dados do cliente no banco
@app.route('/salvar_cliente', methods=['POST'])
def salvar_cliente():
    nome = request.form['nome']
    endereco = request.form['endereco']
    telefone = request.form['telefone']
    email = request.form['email']
    cep = request.form['cep']
    cidade = request.form['cidade']
    estado = request.form['estado']

    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO clientes (nome, endereco, telefone, email, cep, cidade, estado)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (nome, endereco, telefone, email, cep, cidade, estado))
    conn.commit()
    conn.close()

    return redirect('/clientes')



# Lista de clientes
import sqlite3

@app.route('/clientes')
def mostrar_clientes():
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row  # isso faz com que o resultado seja acessível por nome
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return render_template('clientes.html', clientes=clientes)



# Futuras rotas
@app.route("/cadastro_moto")
def cadastro_moto():
    return render_template("cadastro_moto.html")

@app.route("/salvar_moto", methods=["POST"])
def salvar_moto():
    # captura os dados do formulário
    modelo = request.form["modelo"]
    ano = request.form["ano"]
    cor = request.form["cor"]
    chassi = request.form["chassi"]
    placa = request.form["placa"]
    observacoes = request.form["observacoes"]

    # conecta no banco e salva a moto
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO motos (modelo, ano, cor, chassi, placa, observacoes)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (modelo, ano, cor, chassi, placa, observacoes))
    conn.commit()
    conn.close()

    # **IMPORTANTE**: trocar redirecionamento para página de motos cadastradas
    return redirect("/motos_cadastradas")


@app.route('/ordem_servico')
def ordem_servico():
    return render_template('ordem_servico.html')

@app.route('/salvar_ordem', methods=['POST'])
def salvar_ordem():
    dados = request.form
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO ordens_servico (
        nome_oficina, cnpj, endereco_oficina, telefone_oficina,
        nome_cliente, telefone_cliente, endereco_cliente, email_cliente,
        marca, modelo, ano, cor, placa, quilometragem, chassi,
        problema, servicos_pecas, mao_obra, total,
        forma_pagamento, garantia, data_entrada, data_prevista,
        status, observacoes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    dados.get('nome_oficina'),
    dados.get('cnpj'),
    dados.get('endereco_oficina'),
    dados.get('telefone_oficina'),
    dados.get('nome_cliente'),
    dados.get('telefone_cliente'),
    dados.get('endereco_cliente'),
    dados.get('email_cliente'),
    dados.get('marca'),
    dados.get('modelo'),
    dados.get('ano'),
    dados.get('cor'),
    dados.get('placa'),
    dados.get('quilometragem'),
    dados.get('chassi'),
    dados.get('problema'),
    dados.get('servicos_pecas'),
    dados.get('mao_obra'),
    dados.get('total'),
    dados.get('forma_pagamento'),
    dados.get('garantia'),
    dados.get('data_entrada'),
    dados.get('data_prevista'),
    dados.get('status'),
    dados.get('observacoes')
))

    conn.commit()
    conn.close()
    return redirect('/ordens_cadastradas')

@app.route('/ordens_cadastradas')
def ordens_cadastradas():
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ordens_servico")
    ordens = cursor.fetchall()
    conn.close()
    return render_template('ordens_cadastradas.html', ordens=ordens)




# Rota para exibir motos cadastradas
@app.route("/motos_cadastradas")
def motos_cadastradas():
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM motos")
    motos = cursor.fetchall()
    conn.close()
    return render_template("motos_cadastradas.html", motos=motos)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

