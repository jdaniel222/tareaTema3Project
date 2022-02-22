from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, FileField
from wtforms.validators import data_required, length, ValidationError, DataRequired, Length


class FiltroCl(FlaskForm):
    dni = StringField(label="dni", validators=[
        DataRequired(message="El campo es obligatorio"),
        Length(max=10, message="La longitud del DNI no puede superar los 10 caracteres")
    ])

class FormWTF(FlaskForm):
    dni = StringField(label="dni", validators=[
        DataRequired(message="El campo es obligatorio"),
        Length(max=10, message="La longitud del DNI no puede superar los 10 caracteres")
    ])
    nombre = StringField(label="Nombre", validators=[
        DataRequired(message="El campo es obligatorio"),
        Length(min = 5, max = 20, message="El campo debe ser entre 5 y 20 caracteres")
    ])

    apellidos = StringField(label="apellidos", validators=[
        DataRequired(message="El campo es obligatorio"),
        Length(min = 5, max = 50, message="El campo debe ser entre 5 y 50 caracteres")
    ])
    imagen = FileField(label="imagen", validators=[
        DataRequired(message="El campo es obligatorio"),
        FileAllowed(['jpg', 'png'], 'Solo se permiten archivos jpg y png.')
    ])

    # def validate_imagen(form, field):
    #     max_length = 1024*1024
    #     if len(field.data.read()) > max_length:
    #         raise ValidationError(f"El fichero no puede ser superior a {max_length}")
