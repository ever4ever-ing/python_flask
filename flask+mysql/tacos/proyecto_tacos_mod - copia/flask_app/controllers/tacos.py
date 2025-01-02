from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.taco import Taco
from flask_app.models.restaurante import Restaurante

@app.route('/')
def index():
    todos_restaurantes = Restaurante.get_all()  # Expected type: list of Restaurante objects
    
    return render_template("index.html", todos_restaurantes=todos_restaurantes)  # todos_restaurantes is passed to the template

@app.route('/crear',methods=['POST'])
def crear():
    datos = {
        "tortilla":request.form['tortilla'],
        "guiso": request.form['guiso'],
        "salsa": request.form['salsa'],
        "restaurante_id": request.form['restaurante_id']
    }
    Taco.save(datos)
    return redirect('/tacos')

@app.route('/tacos')
def tacos():
    tacos = Taco.get_all()
    todos_restaurantes = Restaurante.get_all()
    return render_template("resultados.html",todos_tacos = tacos, todos_restaurantes = todos_restaurantes)

@app.route('/tacos/restaurante/<int:restaurante_id>')
def tacos_por_restaurante(restaurante_id):
    datos = {
        'restaurante_id': restaurante_id
    }
    tacos = Taco.get_by_restaurante(datos)
    todos_restaurantes = Restaurante.get_all()
    return render_template("resultados.html", todos_tacos=tacos, todos_restaurantes=todos_restaurantes)

@app.route('/restaurante/<int:restaurante_id>/tacos')
def restaurante_y_tacos(restaurante_id):
    datos = {'id': restaurante_id}
    restaurante = Restaurante.get_restaurante_y_tacos(datos)
    return render_template("restaurante_y_tacos.html", restaurante=restaurante)

@app.route('/mostrar/<int:taco_id>')
def detalle(taco_id):
    datos = {
        'id': taco_id
    }
    taco = Taco.get_one(datos)
    return render_template("detalle.html",taco = taco)

@app.route('/editar/<int:taco_id>')
def editar(taco_id):
    datos = {
        'id': taco_id
    }
    taco = Taco.get_one(datos)
    return render_template("editar.html", taco = taco)

@app.route('/actualizar/<int:taco_id>', methods=['POST'])
def actualizar(taco_id):
    datos = {
        'id': taco_id,
        "tortilla":request.form['tortilla'],
        "guiso": request.form['guiso'],
        "salsa": request.form['salsa'],
        "restaurante_id": request.form['restaurante_id']
    }
    Taco.update(datos)
    return redirect(f"/mostrar/{taco_id}")

@app.route('/borrar/<int:taco_id>')
def borrar(taco_id):
    datos = {
        'id': taco_id,
    }
    Taco.delete(datos)
    return redirect('/tacos')
