import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Umasenha2236*'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://usuario:senha@localhost/nome_do_banco'
    SQLALCHEMY_TRACK_MODIFICATIONS = False