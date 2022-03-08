from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import data_required, ValidationError, DataRequired, Length

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