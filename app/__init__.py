from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'secret-jqv'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql10415877:5tATSjznuS@sql10.freemysqlhosting.net:3306/sql10415877'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db = SQLAlchemy(app)


from app.controllers import default
