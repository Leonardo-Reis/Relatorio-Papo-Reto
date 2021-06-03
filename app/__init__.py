from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.secret_key = 'secret-jqv'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'  # 'mysql+pymysql:///sql10415877:5tATSjznuS@sql10.freemysqlhosting.net:3306/sql10415877'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db = SQLAlchemy(app)
ma = Marshmallow(app)

from app.controllers import default
