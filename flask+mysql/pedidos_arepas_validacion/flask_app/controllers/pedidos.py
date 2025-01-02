from flask import render_template, request, redirect, flash
from flask_app.models.pedido import Pedido
from flask_app import app

@app.route('/')
def index():
    pedidos = Pedido.get_all()
    return render_template('pedidos.html', pedidos=pedidos)

@app.route('/nuevo_pedido', methods=['GET'])
def nuevo_pedido():
    return render_template('nuevo_pedido.html')

# Ruta para agregar un nuevo pedido
@app.route('/crear_pedido', methods=['POST'])
def crear_pedido():
    # Validar datos antes de guardar
    data = {
        "nombre_cliente": request.form['nombre_cliente'],
        "cantidad": int(request.form['cantidad']),
        "relleno": request.form['relleno']
    }
    if not Pedido.validar_pedido(data):
        return redirect('/')
    else:
        Pedido.save(data)
        flash("Pedido agregado correctamente", 'success')
        return redirect('/')