from src.app import app
from flask import render_template, request, redirect, url_for


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        # comporobar en base de datos si existe el usuario
        username = request.form.get('username')
        password = request.form.get('password')        
        return redirect(url_for('register'))
    else:
        return render_template('login.html')