from flask import Flask
from flask_recaptcha import ReCaptcha
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .log.logs import configure_logging

app = Flask(__name__)
#Recaptcha
#app.config['RECAPTCHA_SITE_KEY'] = ''
#app.config['RECAPTCHA_SECRET_KEY'] = ''
#recaptcha = ReCaptcha(app)

#se le pasa el nombre de nuestra aplicacion para que los mensajes en el log sean registrados con dicho nombre.
#Objeto logger
logger = configure_logging(__name__)
#Clave secreta
app.secret_key = "claveSecreta"
#conexion
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:123456@localhost:5432/tareaTema3Project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Instanciar un objeto de la clase SQLAlchemy
db = SQLAlchemy(app)
#Instanciar un objeto de la clase Migrate
migrate = Migrate(app,db)
#Instanciar un objeto de la clase LoginManager
login_manager = LoginManager(app)
login_manager.login_view = "login.loginusuario"
#Importamos modelos
from .private.models import Cliente
from .login.models import Usuario

from .public import public
from .private import private
from .login import login
from.admin import admin
def create_app():
    app.register_blueprint(public)
    app.register_blueprint(private)
    app.register_blueprint(login)
    app.register_blueprint(admin)
    return  app