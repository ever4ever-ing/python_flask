from flask_app import app
from flask import render_template, redirect,request,session
from flask_app.models.cancion import Canciones
from flask_app.models.usuario import Usuario
from flask_app.models.favoritos import Favoritos



@app.route('/canciones')
def canciones_index():
    todas_canciones = Canciones.get_all()
    for cancion in todas_canciones:
        cancion.assign_users()  # Asignar usuarios favoritos a cada canción
    return render_template('canciones.html', todas_canciones=todas_canciones)

@app.route('/canciones/agregar', methods=['POST'])
def agregar_cancion():
    data = {
        'titulo': request.form['titulo'],
        'artista': request.form['artista']
    }
    Canciones.agregar_cancion(data)
    return redirect('/canciones')

@app.route('/canciones/<int:id>')
def mostrar_cancion(id):
    cancion = Canciones.get_by_id(id)
    todos_usuarios = Usuario.get_all()

    cancion.assign_users()  # Asignar usuarios favoritos a la canción
    return render_template('mostrar_cancion.html', cancion=cancion, todos_usuarios=todos_usuarios)

@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    datos = {
        'usuario_id': request.form['user_id'],
        'cancion_id': request.form['cancion_id']
    }
    Favoritos.agregar_favorito(datos)
    return redirect('/canciones')