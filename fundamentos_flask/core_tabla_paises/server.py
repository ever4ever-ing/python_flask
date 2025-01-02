from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Datos de ejemplo para la tabla de países y capitales
    paises = [
        {'pais': 'Argentina', 'capital': 'Buenos Aires'},
        {'pais': 'Brasil', 'capital': 'Brasilia'},
        {'pais': 'Chile', 'capital': 'Santiago de Chile'},
        {'pais': 'Colombia', 'capital': 'Bogotá'},
        {'pais': 'Costa Rica', 'capital': 'San José'},
        {'pais': 'Paraguay', 'capital': 'Asunción'},
        {'pais': 'Perú', 'capital': 'Lima'}
    ]
    return render_template('Listas.html', paises=paises)

if __name__ == '__main__':
    app.run(debug=True)
