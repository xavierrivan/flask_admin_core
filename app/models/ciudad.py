from app import db

class Ciudad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    provincia_id = db.Column(db.Integer, db.ForeignKey('provincia.id'), nullable=False)
