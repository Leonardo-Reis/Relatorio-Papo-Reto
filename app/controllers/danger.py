from flask import request, render_template
from app.models.usuarios import User
from app import app, db


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
