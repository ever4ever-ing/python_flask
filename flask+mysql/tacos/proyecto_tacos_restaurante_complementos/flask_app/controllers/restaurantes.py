from flask import render_template
from flask_app import app
from flask_app.models.restaurante import Restaurante

@app.route('/restaurante/<int:restaurante_id>/tacos')
def restaurante_y_tacos(restaurante_id):
    datos = {'id': restaurante_id}
    restaurante = Restaurante.get_restaurante_y_tacos(datos)
    return render_template("restaurante_y_tacos.html", restaurante=restaurante)

@app.route('/restaurantes')
def restaurantes():
    todos_restaurantes = Restaurante.get_all()
    return render_template("restaurantes.html", todos_restaurantes=todos_restaurantes)