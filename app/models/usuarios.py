from app import db, ma


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True)
    senha = db.Column(db.String(40))
    nivel_acesso = db.Column(db.Integer)
    membros = db.relationship('Membro', backref='user', lazy=True)

    def __init__(self, nome, senha, nivel_acesso):
        self.nome = nome
        self.senha = senha
        self.nivel_acesso = nivel_acesso

    def __repr__(self):
        return f"<User {self.nome}>"


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


class Membro(db.Model):
    __tablename__ = 'membro'

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


class MembroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Membro
        load_instance = True


class Relatorio(db.Model):
    __tablename__ = 'relatorio'

    id = db.Column(db.Integer, primary_key=True)
    membro_nome = db.Column(db.String(40), unique=False)
    semana = db.Column(db.Integer, unique=False)
    relatorio = db.Column(db.String(500), default='Relatorio dessa semana não foi enviado', unique=False)
    membro_id = db.Column(db.Integer, db.ForeignKey('membro.id'))

    def __init__(self, membro_nome, semana, relatorio, membro_id):
        self.membro_nome = membro_nome
        self.semana = semana
        self.relatorio = relatorio
        self.membro_id = membro_id

    def __repr__(self):
        return f"<Relatorios {self.membro_nome}>"


class RelatorioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Relatorio
        load_instance = True
