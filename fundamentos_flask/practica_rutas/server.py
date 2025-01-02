from flask import Flask

app = Flask(__name__)

@app.route('/')
def principal():
    return '¡Hola desde Flask!'

@app.route('/rutas')
def ruta():
    return 'Que estas buscando?'

@app.route('/bienvenido/<string:nombre>')
def bienvenido(nombre):
    return f'Bienvenid@ a esta ruta {nombre}'

@app.route('/repite/<int:num>/<string:palabra>')
def repite(num, palabra):
    return f'{palabra} ' * num

@app.errorhandler(404)
def page_not_found(e):
    return "¡Sobrecarga de rutas! No encontramos a donde quieres ir, inténtalo de nuevo.", 404

if __name__ == "__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente
    # Ejecuta la aplicación en modo de depuración/debug para detectar cualquier cambio y recargarlo
    app.run(debug=True)
