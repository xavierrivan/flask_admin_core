# Flask Admin Core

Proyecto MVC en Flask para administrar Ciudades con relación País→Provincia.  

## Características

- Modelos: Pais, Provincia, Ciudad (SQLAlchemy).  
- Validación back‑end: nombre de ciudad único.  
- Dropdowns dependientes (fetch API).  
- Base de datos SQLite (`app.db`).  
- Estructura MVC y Blueprints.  

## Instalación

```bash
git clone <tu-repo-url>
cd flask_admin_core
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python seed.py
python run.py

Uso
Ir a http://127.0.0.1:5000/admin/ciudad/nueva y probar el alta de ciudades.

Deploy
Render.com: conectar repo, start command python run.py.


