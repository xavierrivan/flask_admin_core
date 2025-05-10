# seed.py
from app import create_app, db
from app.models.pais import Pais
from app.models.provincia import Provincia

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()

    # Países
    ecuador   = Pais(nombre='Ecuador')
    argentina = Pais(nombre='Argentina')
    db.session.add_all([ecuador, argentina])
    db.session.flush()

    # Provincias de ejemplo
    db.session.add_all([
        Provincia(nombre='Pichincha',    pais_id=ecuador.id),
        Provincia(nombre='Guayas',       pais_id=ecuador.id),
        Provincia(nombre='Buenos Aires', pais_id=argentina.id),
        Provincia(nombre='Córdoba',      pais_id=argentina.id),
    ])

    db.session.commit()
    print("✅ Seed completado: Países y Provincias creados.")
