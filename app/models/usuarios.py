from app import db, ma


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True)
    senha = db.Column(db.String(40))
    nivel_acesso = db.Column(db.Integer)

    def __init__(self, nome, senha, nivel_acesso):
        self.nome = nome
        self.senha = senha
        self.nivel_acesso = nivel_acesso

    def __repr__(self):
        return f"<User {self.nome}>"


class Membro(db.Model):
    __tablename__ = 'membro'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=False)
    sobrenome = db.Column(db.String(40), unique=False)
    lider_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    lider = db.relationship('User', backref='membros')

    def __init__(self, nome, sobrenome, lider_id):
        self.nome = nome
        self.sobrenome = sobrenome
        self.lider_id = lider_id

    def __repr__(self):
        return f"<Membro {self.nome}>"


class Relatorio(db.Model):
    __tablename__ = 'relatorio'

    id = db.Column(db.Integer, primary_key=True)
    membro_nome = db.Column(db.String(40), unique=False)
    semana = db.Column(db.Integer, unique=False)
    relatorio = db.Column(db.String(500), default='Relatorio dessa semana não foi enviado', unique=False)
    membro_id = db.Column(db.Integer, db.ForeignKey('membro.id'))
    membro = db.relationship('Membro', backref='relatorios')

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

    id = ma.auto_field()
    membro_nome = ma.auto_field()
    semana = ma.auto_field()
    relatorio = ma.auto_field()
    membro_id = ma.auto_field()


class MembroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Membro
        load_instance = True

    id = ma.auto_field()
    nome = ma.auto_field()
    sobrenome = ma.auto_field()
    lider_id = ma.auto_field()

    relatorios = ma.Nested(RelatorioSchema, many=True)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    id = ma.auto_field()
    nome = ma.auto_field()
    senha = ma.auto_field()
    nivel_acesso = ma.auto_field()

    membros = ma.Nested(MembroSchema, many=True)
