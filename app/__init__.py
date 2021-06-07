from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = 'secret-jqv'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql10417477:fTaEanBZ44@sql10.freemysqlhosting.net:3306/sql10417477'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db = SQLAlchemy(app)
ma = Marshmallow(app)

from app.controllers import default, api, danger
