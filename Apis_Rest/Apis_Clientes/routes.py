from Apis_Clientes import app, db
from Apis_Clientes.models import Clientes
from Apis_Clientes.serializer import cliente_schema, clientes_schema
from flask import jsonify, make_response


@app.route("/listar_clientes", methods=["GET"])
def listar_clientes():
    clientes = Clientes.query.all()
    result = clientes_schema.dump(clientes)
    data = {
        'message': 'Todos mis clientes Ok',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data))


@app.route("/cliente_detalle/<int:codigo>", methods=["GET"])
def cliente_detalle(codigo):
    cliente = Clientes.query.get(codigo)
    if cliente:
        result = cliente_schema.dump(cliente)
        data = {
            'message': 'Todos mis clientes Ok',
            'status': 200,
            'data': result
        }
    else:
        data = {
            'message': 'No Existe el Cliente',
            'status': 200
        }
    return make_response(jsonify(data))
