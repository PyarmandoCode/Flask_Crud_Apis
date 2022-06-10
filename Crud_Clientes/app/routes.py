from flask import render_template, request, redirect
from app import app, db
from app.models import Clientes


@app.route('/')
def index():
    # todo queryset traer todos los clientes
    cli = Clientes.query.all()
    # todo pasandole los valores a la plantilla
    return render_template("index.html", cli=cli)


@app.route('/adicionar', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        codigo1 = form.get('codigo')
        nombre1 = form.get('nombre')
        apellido1 = form.get('apellido')
        estado1 = form.get('estado')
        cliente = Clientes(codigo=codigo1, nombre=nombre1, apellido=apellido1, estado=estado1)
        db.session.add(cliente)
        db.session.commit()
        return redirect('/')
    return "Se Grabo el cliente con exito"


@app.route('/eliminar/<int:codigo>')
def eliminar(codigo):
    cliente = Clientes.query.get(codigo)
    if cliente:
        db.session.delete(cliente)
        db.session.commit()
    return redirect('/')


@app.route('/update/<int:codigo>')
def updateRoute(codigo):
    cliente = Clientes.query.get(codigo)
    if cliente:
        return render_template('update.html', cliente=cliente)
    return 'actualizado'


@app.route('/update/<int:codigo>', methods=['POST'])
def update(codigo):
    cliente = Clientes.query.get(codigo)
    if cliente:
        form = request.form
        nombre1 = form.get('nombre')
        apellido1 = form.get('apellido')
        estado1 = form.get('estado')
        cliente.nombre = nombre1
        cliente.apellido = apellido1
        cliente.estado = estado1
        db.session.commit()
    return redirect('/')
