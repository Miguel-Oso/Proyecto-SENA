from src.app import app
from flask import render_template, request, redirect, url_for
from src.models.enums.tipo_documento import TipoDocumento
from src.models.pedidos import Pedido
from flask_controller import FlaskController
from src.models.clientes import Cliente
import datetime

class PedidoController(FlaskController):

    @app.route('/agregar_pedidos', methods=['GET', 'POST'])
    def agregar_pedidos():
        if request.method == 'POST':
            orden_compra = request.form.get('orden_compra')
            fecha_pedido = request.form.get('fecha_pedido')
            fecha_documento = request.form.get('fecha_recibido')
            fecha_despacho = request.form.get('fecha_despacho')
            documento = request.form.get('documento')
            articulo = request.form.get('articulo')
            descripcion = request.form.get('descripcion')
            cantidad = float(request.form.get('cantidad'))
            precio = float(request.form.get('precio'))
            comentarios = request.form.get('comentarios')
            pedido_nuevo = Pedido(orden_compra, fecha_pedido, fecha_documento, fecha_despacho, documento, articulo, descripcion, cantidad, precio, comentarios)
            Pedido.agregar_pedido(pedido_nuevo)
            return redirect(url_for('pedidos'))
        cliente = Cliente.get_all()
        fecha_documento = datetime.datetime.now()
        return render_template('pedidosForm.html', tiposIdentificacion=TipoDocumento, cliente=cliente, fecha_documento=fecha_documento)
    
    @app.route('/pedidos')
    def pedidos():
        pedidos = Pedido.obtener_pedidos()
        return render_template('tablaPedido.html', pedidos=pedidos)