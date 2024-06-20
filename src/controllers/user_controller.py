from src.app import app
from flask import render_template, request, redirect, url_for
from src.models.user_model import User
from src.models.enums.tipo_documento import TipoDocumento
from src.models.enums.rol import Rol
from src.models.enums.estadoUsuario import EstadoUsuario

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        first_name = request.form.get('first_name')
        second_name = request.form.get('second_name')
        first_apellido = request.form.get('first_surname')
        second_apellido = request.form.get('second_surname')
        tipo_documento = request.form.get('tipo_documento')
        documento = request.form.get('documento')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        city = request.form.get('city')
        country = request.form.get('country')
        rol = request.form.get('rol')
        status = request.form.get('status')
        nuevo_usuario = User(username, password, first_name, second_name, first_apellido, second_apellido, tipo_documento, documento, email, phone, address, city, country, rol, status)
        User.save(nuevo_usuario)
        return 'Usuario creado'+ redirect(url_for('login'))
    usuario = User.get_all()
    return render_template('usuarioForm.html', usuario=usuario, tipo_documento=TipoDocumento, roles=Rol, estados=EstadoUsuario)