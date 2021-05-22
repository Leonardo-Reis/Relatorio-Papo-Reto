from Lib.autentificacao import client
from app import app, db

spreadsheets = client('credentials.json')

if __name__ == '__main__':
    db.create_all()
    app.run()
