from flask import render_template, request, redirect, url_for

from models import Usuario
from forms import FormLogin, FormRegistro
from . import login


@login.route("/loginusuario/", methods=["GET", "POST"])
def loginusuario():
    error = ""
    form = FormLogin(request.form)
    if form.validate_on_submit():
        username = form.username.data
    password = form.password.data
    usuario = Usuario.get_by_username(username)
    if usuario and usuario.password == password:
        return redirect(url_for("private.indexcliente"))
    else:
        error = "Usuario y/o contraseña incorrecta"

    return render_template("loginusuario.html", form=form, error=error)


