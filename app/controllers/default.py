from app import app, db
from flask import request, render_template, session, redirect, url_for, flash
from Lib.autentificacao import client
from app.models.usuarios import User, Grupo
import pandas as pd

spreadsheets = client('credentials.json')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome'].lower().strip()
        senha = request.form['senha'].strip()
        check_nome = User.query.filter_by(nome=nome).first()
        if check_nome:
            if check_nome.senha == senha:
                session['nome'] = nome
                session['senha'] = senha
                return redirect(url_for('usuario'))
            else:
                flash('Senha incorreta')
        else:
            flash('Usuario não encontrado')
    return render_template('index.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if session:
        if request.method == 'POST':
            nome = request.form['nome'].strip().lower()
            senha = request.form['senha'].strip()
            nivel_acesso = request.form['nivel-acesso']

            user = User(nome=nome, senha=senha, nivel_acesso=nivel_acesso)
            db.session.add(user)
            db.session.commit()

        return render_template('cadastro.html')
    else:
        return redirect(url_for('index'))


@app.route('/usuario')
def usuario():
    if session:
        return render_template('usuario.html')
    else:
        return redirect(url_for('index'))


@app.route('/usuario/novomembro', methods=['GET', 'POST'])
def novomembro():
    if session:
        if request.method == 'POST':
            nome = request.form['nome'].strip().lower()
            sobrenome = request.form['sobrenome'].strip().lower()
            lider_id = User.query.filter_by(nome=session['nome']).first().id

            novo_membro = Grupo(nome=nome, sobrenome=sobrenome, lider_id=lider_id)

            db.session.add(novo_membro)
            db.session.commit()

            print('foi')

        return render_template('novomembro.html')
    else:
        return redirect(url_for('index'))


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
