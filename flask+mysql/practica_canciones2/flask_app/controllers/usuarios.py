from flask_app import app
from flask import render_template, redirect,request,session
from flask_app.models.usuario import Usuario
from flask_app.models.cancion import Canciones
from flask_app.models.favoritos import Favoritos

@app.route('/')
def main():
    todos_usuarios = Usuario.get_all()
    return render_template('usuarios.html', todos_usuarios = todos_usuarios)

@app.route('/usuarios/<int:id>')
def mostrar_usuario(id):
    data = {
        'id': id
    }
    print("el id del usuario es:",data)
    todas_canciones = Canciones.get_all()
    for cancion in todas_canciones:
        print(cancion.titulo)

    usuario = Usuario.get_canciones_y_usuarios(data)
    print("las canciones favoritas del usuario son:")
    for cancion in usuario.mis_favoritas:
        print(cancion)

    return render_template('mostrar_usuario.html', todas_canciones = todas_canciones, usuario = usuario)


@app.route('/agregar_favorita', methods=['POST'])
def agregar_favorita():
    print("se esta agregando una cancion favorita")
    print(request.form)
    datos = {
        'usuario_id': request.form['usuario_id'],
        'cancion_id': request.form['cancion_id']
    }
    print(datos)
    Favoritos.agregar_favorito(datos)
    return redirect(f"/usuarios/{request.form['usuario_id']}")