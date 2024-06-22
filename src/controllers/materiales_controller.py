from src.app import app
from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController
from src.models.enums.unidadMedida import UnidadMedida
from src.models.materiales_model import Material
import datetime

class MaterialesController(FlaskController):
    
        @app.route('/agregar_material', methods=['GET', 'POST'])
        def agregar_material():
            if request.method == 'POST':
                fecha_pedido = request.form.get('fecha_pedido')
                fecha_recibido = request.form.get('fecha_recibido')
                codigo = request.form.get('codigos')
                nombre = request.form.get('material')
                referencia = request.form.get('referencia')
                proveedor = request.form.get('proveedor')
                descripcion = request.form.get('descripcion')
                producto_final = request.form.get('producto_final')
                cantidad = request.form.get('cantidad')
                unidad_medida = request.form.get('unidad_medida')
                comentarios = request.form.get('comentarios')
                material_nuevo = Material(fecha_pedido, fecha_recibido, codigo, nombre, referencia, proveedor, descripcion, producto_final, cantidad, unidad_medida, comentarios)
                Material.agregar_material(material_nuevo)
                return redirect(url_for('materiales'))
            fecha_recibido = datetime.datetime.now()
            return render_template('materialesForm.html', undMedida=UnidadMedida, fecha_recibido=fecha_recibido)
    
        @app.route('/materiales')
        def materiales():
            materiales = Material.obtener_materiales()
            return render_template('tablaMateriales.html', materiales=materiales)