from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True)
    senha = db.Column(db.String)
    # nivel_acesso = db.Column(db.Integer)

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        # self.nivel_acesso = nivel_acesso

    def __repr__(self):
        return f"<User {self.nome}>"
