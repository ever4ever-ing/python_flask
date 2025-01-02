from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash

from flask_app.models.usuario import Usuario #Importamos la clase

@app.route("/")
def index():
    usuarios = Usuario.get_all()
    return render_template("index.html", usuarios=usuarios)

@app.route("/nuevo_usuario", methods=["GET"])
def nuevo_usuario():
    return render_template("nuevo_usuario.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    if not Usuario.validar_usuario(data):#Valida los datos
        return redirect("/nuevo_usuario")#Si no es valido, redirige al formulario
    else:
        Usuario.save(data)
        return redirect("/")

@app.route("/usuarios/<int:id>")
def ver_usuario(id):
    usuario = Usuario.get_by_id(id)
    return render_template("ver_usuario.html", usuario=usuario)

@app.route("/usuarios/editar/<int:id>", methods=["GET"])
def editar_usuario(id):
    usuario = Usuario.get_by_id(id)
    return render_template("editar_usuario.html", usuario=usuario)

@app.route("/usuarios/actualizar/<int:id>", methods=["POST"])
def actualizar_usuario(id):
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"],
        "id": id
    }
    ##Validar datos
    if not Usuario.validar_usuario(data):
        return redirect(f"/usuarios/editar/{id}")
    Usuario.update(data)
    return redirect("/")

@app.route("/usuarios/eliminar/<int:id>")
def borrar_usuario(id):
    Usuario.delete(id)
    return redirect("/")