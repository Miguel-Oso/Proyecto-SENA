from src.app import app
from flask import render_template, request, redirect, url_for
from src.models.clientes import Cliente
from src.models.enums.tipo_documento import TipoDocumento

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':
        tipo_documento = request.form.get('tipo_documento')
        documento = request.form.get('documento')
        nombre = request.form.get('nombre')
        ciudad = request.form.get('ciudad')
        direccion = request.form.get('direccion')
        correo = request.form.get('correo')
        telefono = request.form.get('telefono')
        nuevo_cliente = Cliente(tipo_documento, documento, nombre, ciudad, direccion, correo, telefono)
        Cliente.save(nuevo_cliente)
        return redirect(url_for('clientes'))
    clientes = Cliente.get_all()
    return render_template('clientesForm.html', tiposIdentificacion=TipoDocumento, clientes=clientes)
