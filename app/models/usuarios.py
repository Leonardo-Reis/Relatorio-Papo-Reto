from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True)
    senha = db.Column(db.String)
    nivel_acesso = db.Column(db.Integer)
    membros = db.relationship('Membro', backref='user', lazy=True)

    def __init__(self, nome, senha, nivel_acesso):
        self.nome = nome
        self.senha = senha
        self.nivel_acesso = nivel_acesso

    def __repr__(self):
        return f"<User {self.nome}>"


class Membro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=False)
    sobrenome = db.Column(db.String(40), unique=False)
    lider_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    relatorios = db.relationship('Relatorio', backref='membro', lazy=True)

    def __init__(self, nome, sobrenome, lider_id, lider_nome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.lider_id = lider_id
        self.lider_nome = lider_nome

    def __repr__(self):
        return f"<Membro {self.nome}>"


class Relatorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    membro_nome = db.Column(db.String(40), unique=False)
    semana = db.Column(db.Integer, unique=False)
    relatorio = db.Column(db.String(), unique=False)
    membro_id = db.Column(db.Integer, db.ForeignKey('membro.id'))

    def __init__(self, membro_nome, semana, relatorio, membro_id):
        self.membro_nome = membro_nome
        self.semana = semana
        self.relatorio = relatorio
        self.membro_id = membro_id

    def __repr__(self):
        return f"<Relatorios {self.membro_nome}>"
