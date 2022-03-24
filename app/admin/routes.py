from flask import render_template
from flask_login import login_required, current_user
from ..auth.decorators import admin_required
from . import admin
from ..login.models import Usuario
import app

@admin.route("/adminindex/", methods=["GET","POST"])
@login_required
@admin_required
def adminindex():
    return render_template('adminindex.html')

@admin.route("/listadousuarios/", methods=["GET","POST"])
@login_required
@admin_required
def listadousuarios():
    usuario = Usuario.query.filter_by(is_admin=False)
    return render_template('listadousuarios.html', usuario=usuario)

@admin.errorhandler(401)
def page_not_fount(error):
    if not current_user.is_admin:
        app.logger.warning(f"Acceso no autorizado al area de administración: {current_user}")
    return "Accesso no permitido", 401