from flask import render_template
from flask_login import login_required
from ..auth.decorators import admin_required
from . import admin
from ..login.models import Usuario


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