from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

import app
from .models import Usuario
from .forms import FormLogin, FormRegistro
from . import login
from .checkv import Checkv

prueba = Checkv()

@login.route('/registrousuario/', methods=["GET", "POST"])
def registrousuario():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
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
            app.logger.info(f"Registro usuario: Nombre de usuario: {form.username.data} ya existente")
        else:
            usuario.username = form.username.data
            if app.ReCaptcha.verify():
                usuario.create()
                return redirect(url_for("login.loginusuario"))
    return render_template("registrousuario.html", form=form, errorExist=errorExist)

@login.route("/loginusuario/", methods=["GET", "POST"])
def loginusuario():
    error = ""
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    form = FormLogin(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        usuario = Usuario.get_by_username(username)
        if usuario and usuario.check_password(password) and app.ReCaptcha.verify():
            prueba.resetAttemps()  # attemps 0
            login_user(usuario, form.recuerdame.data)
            return redirect(url_for("private.indexcliente"))
        else:
            prueba.attemps+=1
            error = "Usuario y/o contraseña incorrecto"
            app.logger.error(f"Login: Intento de acceso usuario: {username} Nª Intentos {prueba.attemps}")
    return render_template("loginusuario.html", form=form, error=error)

@app.login_manager.user_loader
def load_user(user_id):
    return Usuario.get_by_id(user_id)

@login.route("/logoutsession/")
def logoutsession():
    logout_user()
    return redirect(url_for('login.loginusuario'))

