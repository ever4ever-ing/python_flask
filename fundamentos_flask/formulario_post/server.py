from flask import Flask, render_template, request, redirect, session 

app = Flask(__name__)
app.secret_key = 'Esta es tu clave secreta!' #Establecemos una clave secreta

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/crear_usuario', methods=['POST'])
def crear():
    print("Recibiendo información")
    session['nombre_usuario'] = request.form['nombre']
    session['email_usuario'] = request.form['email']
    # JAMAS renderizamos una plantilla ante una solicitud POST
    return redirect('/mostrar_usuario')  # En su lugar, redirigimos a otra ruta

@app.route('/mostrar_usuario')
def mostrar_usuario():
    print("Usuario redirigido")
    # Imprime un diccionario vacío, porque no tenemos acceso a esta información
    print(session['nombre_usuario'])
    return render_template("mostrar.html", nombre=session['nombre_usuario'])

if __name__ == "__main__":
    app.run(debug=True)
