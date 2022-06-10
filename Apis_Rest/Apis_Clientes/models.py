from Apis_Clientes import db


class Clientes(db.Model):
    codigo = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60))
    apellido = db.Column(db.String(60))
    estado = db.Column(db.String(5))

    def __init__(self, codigo, nombre, apellido, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.estado = estado


# todo crear el modelo dentro de la Base de datos
db.create_all()
