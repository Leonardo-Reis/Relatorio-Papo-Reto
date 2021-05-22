from app import app
from app import db
from flask import request, render_template
from Lib.autentificacao import client
from app.models.usuarios import User
import pandas as pd

spreadsheets = client('credentials.json')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/enviar', methods=['GET', 'POST'])
def enviar():
    if request.method == 'POST':
        sp_nomes_pprt = spreadsheets.open('nomes-papo-reto')
        ws_nomes_pprt = sp_nomes_pprt.worksheet('nomes')
        df_nomes_pprt = pd.DataFrame(ws_nomes_pprt.get_all_records())

        nome = request.form['nome'].capitalize().strip()
        sobrenome = request.form['sobrenome'].capitalize().strip()
        linha = {"nome": nome, "sobrenome": sobrenome}

        df = df_nomes_pprt.append(linha, ignore_index=True)

        ws_nomes_pprt.update([df.columns.values.tolist()] + df.values.tolist())
    return render_template('enviar.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        user = User(nome=nome, senha=senha)
        db.session.add(user)
        db.session.commit()

    return render_template('cadastro.html')


@app.route('/teste')
def teste():
    nome = User.query.filter_by(nome='leonardo').first()
    print(nome)
    return 'lol'