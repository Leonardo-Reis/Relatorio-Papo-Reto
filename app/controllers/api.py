from flask import session, jsonify, request, render_template, redirect, url_for
from app.models.usuarios import User, MembroSchema, UserSchema
from Lib.autentificacao import client
from app import app
import pandas as pd

spreadsheets = client('credentials.json')


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
        return 'Faça login'


@app.route('/api/<usuario>')
def retornaUser(usuario):
    if session:
        user = User.query.filter_by(nome=usuario).first()
        user_schema = UserSchema()
        output = user_schema.dump(user)
        return jsonify({'output': output})

    else:
        return 'Login não realizado'


@app.route('/enviar', methods=['GET', 'POST'])
def enviar():
    if session:
        lider = User.query.filter_by(id=session['id']).first()
        if request.method == 'POST':
            sp_nomes_pprt = spreadsheets.open('nomes-papo-reto')
            try:
                ws_nomes_pprt = sp_nomes_pprt.worksheet(session['nome'])
            except:
                sp_nomes_pprt.add_worksheet(session['nome'], rows=50, cols=50)
                ws_nomes_pprt = sp_nomes_pprt.worksheet(session['nome'])

            df_nomes_pprt = pd.DataFrame(ws_nomes_pprt.get_all_records())

            nome = request.form['nome'].capitalize().strip()
            sobrenome = request.form['sobrenome'].capitalize().strip()

            linha = {"Nome": f'{nome} {sobrenome}', 'Semana 1': '', 'Semana 2': '', 'Semana 3': '', 'Semana 4': ''}

            df = df_nomes_pprt.append(linha, ignore_index=True)
            ws_nomes_pprt.update([df.columns.values.tolist()] + df.values.tolist())

        return render_template('enviar.html')
    else:
        return redirect(url_for('index'))
