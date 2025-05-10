from app import db

class Pais(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    provincias = db.relationship('Provincia', backref='pais', lazy=True)
