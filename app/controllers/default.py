from app import app, db
from flask import request, render_template, session, redirect, url_for, flash
from app.models.usuarios import User, Membro, Relatorio


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
                session['id'] = check_nome.id
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
    membros = User.query.filter_by(nome=session['nome']).first().membros
    return render_template('grupo.html', membros=membros)


@app.route('/usuario/grupo/relatorios')
def grupo_relatorios():
    if session:
        membros = User.query.filter_by(nome=session['nome']).first().membros
        return render_template('grupo-relatorios.html', variaveis=[membros, Relatorio])
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


@app.route('/logout')
def logout():
    if session:
        session.clear()
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
