from app import app, db
from flask import request, render_template, session, redirect, url_for, flash, jsonify
from app.models.usuarios import User, Membro, Relatorio, UserSchema, MembroSchema
# from Lib.autentificacao import client
# import pandas as pd

# spreadsheets = client('credentials.json')


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
        print(User.query.all())
        return render_template('usuario.html')
    else:
        return redirect(url_for('index'))


@app.route('/usuario/novomembro', methods=['GET', 'POST'])
def novomembro():
    if session:
        if request.method == 'POST':
            nome = request.form['nome'].strip().lower()
            sobrenome = request.form['sobrenome'].strip().lower()
            lider = User.query.filter_by(nome=session['nome']).first()

            lider_id = lider.id

            novo_membro = Membro(nome=nome, sobrenome=sobrenome, lider_id=lider_id)

            db.session.add(novo_membro)
            db.session.commit()

            print('foi')

        return render_template('novomembro.html')
    else:
        return redirect(url_for('index'))


@app.route('/usuario/grupo')
def grupo():
    if session:
        membros = User.query.filter_by(nome=session['nome']).first().membros
        return render_template('grupo.html', variaveis=[membros, Relatorio])
    else:
        return redirect(url_for('index'))


@app.route('/usuario/relatorio', methods=['POST', 'GET'])
def relatorio():
    if session:
        lider = User.query.filter_by(nome=session['nome']).first()
        membros = lider.membros
        if request.method == 'POST':
            for membro in membros:
                nome = membro.nome
                relatorio = request.form[f'{membro.nome}']
                semana = int(request.form['semana'])

                novo_relatorio = Relatorio(membro_nome=nome, relatorio=relatorio, semana=semana, membro_id=membro.id)

                db.session.add(novo_relatorio)
                db.session.commit()

        return render_template('relatorio.html', membros=membros)
    else:
        return redirect(url_for('index'))


@app.route('/api/<usuario>')
def getbanco(usuario):
    if session:
        user = User.query.filter_by(nome=usuario).first()
        user_schema = UserSchema()
        output = user_schema.dump(user)
        return jsonify({'user': output})
    else:
        return 'Login não realizado'


@app.route('/api/<usuario>/<membroparam>')
def getmembro(usuario=None, membroparam=None):
    if session:
        user = User.query.filter_by(nome=usuario).first()
        membro_output = None

        for membro in user.membros:
            if membro.nome == membroparam:
                membro_output = membro

        if membro_output is not None:
            membro_schema = MembroSchema()
            output = membro_schema.dump(membro_output)
            return output
        else:
            return 'O membro especificado para esse lider de grupo não existe ou não foi registrado.'
    else:
        return 'Login não realizado'


@app.route('/<usuario>')
def retornaUser(usuario):
    user = User.query.filter_by(nome=usuario).first()
    user_schema = UserSchema()
    output = user_schema.dump(user)
    print(output['membros'])
    return jsonify({'user': output})


@app.route('/logout')
def logout():
    if session:
        session.clear()
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


# @app.route('/enviar', methods=['GET', 'POST'])
# def enviar():
#    if request.method == 'POST':
#        sp_nomes_pprt = spreadsheets.open('nomes-papo-reto')
#        ws_nomes_pprt = sp_nomes_pprt.worksheet('nomes')
#        df_nomes_pprt = pd.DataFrame(ws_nomes_pprt.get_all_records())
#
#        nome = request.form['nome'].capitalize().strip()
#        sobrenome = request.form['sobrenome'].capitalize().strip()
#        linha = {"nome": nome, "sobrenome": sobrenome}
#
#        df = df_nomes_pprt.append(linha, ignore_index=True)
#
#        ws_nomes_pprt.update([df.columns.values.tolist()] + df.values.tolist())
#    return render_template('enviar.html')


@app.route('/cadastro-forcado', methods=['POST', 'GET'])
def forcado():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        nivel_acesso = request.form['nivel-acesso']

        user = User(nome=nome, senha=senha, nivel_acesso=nivel_acesso)
        db.session.add(user)
        db.session.commit()
    return render_template('forcado.html')


@app.route('/usuario/apagar-banco', methods=['GET', 'POST'])
def apagarBanco():
    if request.method == 'POST':
        db.drop_all()
        db.create_all()
    return render_template('apagar.html')
