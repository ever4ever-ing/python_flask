# /app/app.py
from flask import Flask, render_template
from models.usuario import Usuario

app = Flask(__name__)
@app.route("/")
@app.route("/usuarios")
def listar_usuarios():
    usuarios = Usuario.obtener_todos()
    return render_template("usuarios.html", usuarios=usuarios)

@app.route("/usuarios/<int:usuario_id>/favoritos")
def favoritos_usuario(usuario_id):
    favoritos = Usuario.obtener_favoritos(usuario_id)
    print(favoritos)
    return render_template("favoritos.html", favoritos=favoritos)

if __name__ == "__main__":
    app.run(debug=True)
