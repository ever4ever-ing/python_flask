from flask import Flask, request, redirect, render_template

from usuario import Usuario

app = Flask(__name__)


@app.route("/")
def index():
    usuarios = Usuario.get_all()
    for usuario in usuarios:
        print(usuario.nombre)
    return render_template("index.html", usuarios=usuarios)


@app.route("/nuevo_usuario", methods=["GET"])
def nuevo_usuario():
    return render_template("nuevo_usuario.html")


@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():

    datos = {
        "nombre": request.form['nombre'],
        "email": request.form["email"],
        "apellido": request.form["apellido"]
    }
    # Enviamos el diccionario al metodo save de Mascota
    Usuario.save(datos)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
