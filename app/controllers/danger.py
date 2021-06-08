from flask import request, render_template
from app.models.usuarios import User
from app import app, db


@app.route('/cadastro-forcado', methods=['POST', 'GET'])
def forcado():
    if request.method == 'POST':
        nome = request.form['nome'].strip().lower()
        senha = request.form['senha'].strip()
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
