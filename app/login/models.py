from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    nombre = db.Column(db.String(20), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        try:
            db.session.commit()
        except:
            raise


    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)

    @staticmethod
    def get_by_username(username):
        return Usuario.query.filter_by(username=username).first()

    def check_username(self, username):
        if self.username == username:
            return True
        else:
            return False

    def set_password(self, password):
        method = "pbkdf2:sha256:260000"
        self.password = generate_password_hash(password, method=method)

    def check_password(self, password):
        if check_password_hash(self.password, password):
            return True
        else:
            return False
