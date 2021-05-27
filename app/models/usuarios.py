from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True)
    senha = db.Column(db.String)
    nivel_acesso = db.Column(db.Integer)
    monitorados = db.relationship('Grupo', backref='user', lazy=True)

    def __init__(self, nome, senha, nivel_acesso):
        self.nome = nome
        self.senha = senha
        self.nivel_acesso = nivel_acesso

    def __repr__(self):
        return f"<User {self.nome}>"


class Grupo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=False)
    sobrenome = db.Column(db.String(40), unique=False)
    lider_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, nome, sobrenome, lider_id, lider_nome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.lider_id = lider_id
        self.lider_nome = lider_nome

    def __repr__(self):
        return f"<Grupo {self.lider_id}>"
