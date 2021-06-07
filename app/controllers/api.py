from flask import session, jsonify
from app.models.usuarios import User, MembroSchema, UserSchema
from app import app


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
        return jsonify({'user': output})

    else:
        return 'Login não realizado'
