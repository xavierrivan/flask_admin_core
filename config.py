import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Clave secreta para sesiones y CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY', 'cambia-esta-clave-por-una-segura')

    # Base de datos SQLite en archivo app.db en la raíz
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
