import base64

from flask import render_template, request, redirect, url_for
from werkzeug.datastructures import CombinedMultiDict
from werkzeug.utils import secure_filename

from .models import Cliente
from .forms import FormWTF, FiltroCl
from . import private


@private.route("/indexcliente/", methods=["GET","POST"])
def indexcliente():
    filtro = FiltroCl(request.form)
    if filtro.validate_on_submit():
        dni = filtro.dni.data
        cliente = Cliente.query.filter_by(dni=dni)
        return render_template("indexcliente.html", filtro=filtro, clientes=cliente)
    else:
        clientes = Cliente.query.all()
        return render_template("indexcliente.html", filtro=filtro, clientes=clientes)

@private.route("/createcliente/", methods=["GET","POST"])
def createcliente():
    form = FormWTF(CombinedMultiDict((request.files, request.form)))
    if form.validate_on_submit():
    #recoger datos de formulario e insertar en la BD
        cliente = Cliente()
        cliente.dni = form.dni.data
        cliente.nombre = form.nombre.data
        cliente.apellidos = form.apellidos.data

        encoded_bytes = base64.b64encode(form.imagen.data.read())

        if len(encoded_bytes)>1024*1024:
            form.imagen.errors.append("Tamaño maximo 1MB")
            return render_template("createcliente.hmtl", form=form)

        cliente.imagen = str(encoded_bytes).replace("b'", "").replace("'", "")

        cliente.crearCliente()
        return redirect(url_for('private.indexcliente'))



    return render_template('createcliente.html', form=form)




