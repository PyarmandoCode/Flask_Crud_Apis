# class Config(object):
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///bdclientes.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = True


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@localhost:5432/clientes_bd'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
