from flask import render_template, request, redirect, url_for

from .models import Usuario
from .forms import FormLogin, FormRegistro
from . import login
from app import private

@login.route('/registrousuario/', methods=["GET", "POST"])
def registrousuario():
    form = FormRegistro(request.form)
    if form.validate_on_submit():
        usuario = Usuario()
        usuario.username = form.username.data
        usuario.set_password(form.password.data)
        usuario.nombre = form.nombre.data
        usuario.apellidos = form.apellidos.data
        usuario.create()
        return redirect(url_for("private.loginusuario"))

    return render_template("registrousuario.html", form=form)


@login.route("/loginusuario/", methods=["GET", "POST"])
def loginusuario():
    error = ""
    form = FormLogin(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        usuario = Usuario.get_by_username(username)
        if usuario and usuario.check_password(password):
            return redirect(url_for("private.indexcliente"))
        # if usuario and usuario.password == password:
        #     return redirect(url_for("private.indexcliente"))
        else:
            error = "Usuario y/o contraseña incorrecta"

    return render_template("loginusuario.html", form=form, error=error)
