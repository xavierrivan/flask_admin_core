from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app import db
from app.models.pais import Pais
from app.models.provincia import Provincia
from app.models.ciudad import Ciudad

admin_bp = Blueprint('admin', __name__, template_folder='../templates')

@admin_bp.route('/ciudad/nueva', methods=['GET', 'POST'])
def nueva_ciudad():
    paises = Pais.query.order_by(Pais.nombre).all()
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        provincia_id = request.form['provincia']
        # 🚨 Validación backend: nombre único
        if Ciudad.query.filter_by(nombre=nombre).first():
            flash("🚨 Error: la ciudad ya existe.", "error")
            return redirect(url_for('admin.nueva_ciudad'))
        c = Ciudad(nombre=nombre, provincia_id=provincia_id)
        db.session.add(c)
        db.session.commit()
        flash("Ciudad creada correctamente.", "success")
        return redirect(url_for('admin.nueva_ciudad'))
    return render_template('ciudad_form.html', paises=paises)

@admin_bp.route('/provincias/<int:pais_id>')
def provincias(pais_id):
    provs = Provincia.query.filter_by(pais_id=pais_id).order_by(Provincia.nombre).all()
    return jsonify([{'id': p.id, 'nombre': p.nombre} for p in provs])
