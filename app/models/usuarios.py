from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True)
    senha = db.Column(db.String)
    nivel_acesso = db.Column(db.Integer)

    def __init__(self, nome, senha, nivel_acesso):
        self.nome = nome
        self.senha = senha
        self.nivel_acesso = nivel_acesso

    def __repr__(self):
        return f"<User {self.nome}>"


class Grupo(db.Model):
    __tablename__ = 'grupo'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=False)
    lider_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    lider = db.relatio
    nship('User', foreign_keys=lider_id)

    def __init__(self, nome, lider_id):
        self.nome = nome
        self.lider_id = lider_id

    def __repr__(self):
        return f"<Grupo {self.lider.nome}>"
