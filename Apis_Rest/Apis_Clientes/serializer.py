from Apis_Clientes import app
from Apis_Clientes.models import Clientes

from flask_marshmallow import Marshmallow

ma = Marshmallow(app)


class ClienteSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Clientes
        filds = ('codigo', 'nombre', 'apellido', 'estado')


cliente_schema = ClienteSerializer()

clientes_schema = ClienteSerializer(many=True)
