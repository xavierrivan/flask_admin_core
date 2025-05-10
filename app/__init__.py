# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Instancia de la base de datos
db = SQLAlchemy()

def create_app():
    # 1) Crear la aplicación
    app = Flask(__name__)
    # 2) Cargar configuración
    app.config.from_object(Config)
    # 3) Inicializar extensión de base datos
    db.init_app(app)

    # 4) Registrar el blueprint de administración
    from app.routes.admin import admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    # 5) Crear tablas si no existen
    with app.app_context():
        db.create_all()

    return app
