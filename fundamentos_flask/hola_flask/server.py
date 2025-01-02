from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación

# Crea una nueva instancia de la clase Flask llamada "app"
app = Flask(__name__)

# El decorador "@" asocia esta ruta con la función inmediatamente siguiente

@app.route('/')  # La ruta raíz, es decir, 'localhost:5000/'
def hola_mundox():
    return '¡Hola Mundoooooo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/exito')
def exito():  # El nombre de la función puede ser el que tú quieras
    return '¡Éxito!'  # Devuelve la cadena '¡Éxito!' como respuesta

@app.route('/color/<nombre>/<color>')
def color_favorito(nombre, color):
    print(nombre)
    print(color)
    return f'Hola {nombre}, tu color favorito es el {color}'

@app.route('/saludo/<nombre>/<int:num>')
def hola_cantidad(nombre, num):
    return f'¡Hola {nombre}!'*num 

if __name__ == "__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente
    # Ejecuta la aplicación en modo de depuración/debug para detectar cualquier cambio y recargarlo
    app.run(debug=True)
