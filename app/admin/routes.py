from os import abort

from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required
from ..auth.decorators import admin_required
from . import admin
from ..login.models import Usuario


@admin.route("/adminindex/", methods=["GET","POST"])
@login_required
@admin_required
def adminindex():
#    if not current_user.is_admin:
#        abort(401)
    return render_template('adminindex.html')


@admin.route("/listadousuarios/", methods=["GET","POST"])
@login_required
@admin_required
def listadousuarios():
    if not current_user.is_admin:
        abort(401)
    usuario = Usuario.query.filter_by(is_admin=False)
    return render_template('listadousuarios.html', usuario=usuario)