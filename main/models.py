from main import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    exp = db.Column(db.Integer, index=True, unique=True)
    nombre = db.Column(db.String(200))
    solicitud = db.Column(db.String(100))
    tramite = db.Column(db.String(150))
    correo = db.Column(db.String(100))
    celular = db.Column(db.String(50))

    def __repr__(self):
        return f'<User {self.exp}>'
