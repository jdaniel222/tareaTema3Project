from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, FileField, PasswordField
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
        Length(min=5, max=20, message="El campo debe ser entre 5 y 20 caracteres")
    ])

    apellidos = StringField(label="apellidos", validators=[
        DataRequired(message="El campo es obligatorio"),
        Length(min=5, max=50, message="El campo debe ser entre 5 y 50 caracteres")
    ])
    imagen = FileField(label="imagen", validators=[
        DataRequired(message="El campo es obligatorio"),
        FileAllowed(['jpg', 'png'], 'Solo se permiten archivos jpg y png.')
    ])

    # def validate_imagen(form, field):
    #     max_length = 1024*1024
    #     if len(field.data.read()) > max_length:
    #         raise ValidationError(f"El fichero no puede ser superior a {max_length}")

class FormLogin(FlaskForm):
    username = StringField(label="Nombre de usuario", validators=[
        DataRequired(message="El nombre de usuario es obligatorio"),
        Length(max=20, message="El nombre de usuario no puede ser superior a 20 caracteres")
    ])
    password = PasswordField(label="Contraseña", validators=[
        DataRequired(message="La contraseña es obligatoria"),
        Length(min=8, message="La contraseña no puede ser inferior a 8 caracteres")
    ])

class FormRegistro(FlaskForm):
    username = StringField(label="Nombre de usuario", validators=[
        DataRequired(message="El nombre de usuario es obligatorio"),
        Length(max=15, message="El nombre de usuario no puede ser superior a 15 caracteres")
    ])
    password = PasswordField(label="Contraseña", validators=[
        DataRequired(message="La contraseña es obligatoria"),
        Length(min=8, message="La contraseña no puede ser inferior a 8 caracteres")
    ])
    passwordRepeat = PasswordField(label="Repita la contraseña", validators=[
        DataRequired(message="contraseña es obligatoria"),
        Length(min=8, message="La contraseña no puede ser inferior a 8 caracteres")
    ])
    dni = StringField(label="DNI", validators=[
        DataRequired(message="El DNI es obligatorio"),
        Length(max=10, message="El DNI no puede ser superior a 10 caracteres")
    ])
    nombre = StringField(label="Nombre", validators=[
        DataRequired(message="El nombre es obligatorio"),
        Length(max=10, message="El nombre no puede ser superior a 20 caracteres")
    ])
    apellidos = StringField(label="Apellidos", validators=[
        DataRequired(message="El nombre es obligatorio"),
        Length(max=50, message="El nombre no puede ser superior a 50 caracteres")
    ])
    # submit = SubmitField(label="Dar de alta")

    def validate_password(form,field):
        if (field.data).isdigit():
            raise ValidationError("La contraseña no pueden ser solo digitos")
        if field.data != form.passwordRepeat.data:
            raise ValidationError("Las contraseñas no coinciden")

    def validate_passwordRepeat(form, field):
        if field.data != form.password.data:
            raise ValidationError("Las contraseñas no coinciden")
