from flask import render_template, request, redirect, url_for

from .models import Usuario
from .forms import FormLogin, FormRegistro
from . import login


@login.route('/registrousuario/', methods=["GET", "POST"])
def registrousuario():
    errorExist = ""
    form = FormRegistro(request.form)
    if form.validate_on_submit():
        usuario = Usuario()
        usuario.set_password(form.password.data)
        usuario.nombre = form.nombre.data
        usuario.apellidos = form.apellidos.data
        username = usuario.get_by_username(form.username.data)
        if username:
            errorExist = "Nombre de usuario no disponible"
        else:
            usuario.username = form.username.data
            usuario.create()
            return redirect(url_for("login.loginusuario"))
    return render_template("registrousuario.html", form=form, errorExist=errorExist)


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


