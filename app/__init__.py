from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.secret_key = "clave"

#conexion
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:123456@localhost:5432/tareaTema3Project'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#instaciar un objeto de la clase SQLAlchemy
db = SQLAlchemy(app)
#Incanciar un objeto de la clase Migrate
migrate = Migrate(app,db)
#Importamos modelo
from .private.models import Cliente
from .login.models import Usuario

from .public import public
from .private import private
from .login import login

def create_app():
    app.register_blueprint(public)
    app.register_blueprint(private)
    app.register_blueprint(login)
    return  app
