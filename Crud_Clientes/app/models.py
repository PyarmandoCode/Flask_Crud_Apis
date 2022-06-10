from app import  db

class Clientes(db.Model):
    codigo = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(60))
    apellido = db.Column(db.String(60))
    estado = db.Column(db.String(5))


#todo crear el modelo dentro de la Base de datos
db.create_all()