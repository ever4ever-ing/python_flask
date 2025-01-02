from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Página principal


@app.route('/')
def index():
    return render_template('index.html')

# Procesar nombre (del ejemplo original)


@app.route('/process', methods=['POST'])
def process():
    data = request.json
    name = data.get('name', '')
    if name:
        response = {"message": f"Hola, {name}!"}
    else:
        response = {"message": "Por favor, introduce un nombre."}
    return jsonify(response)

# Nuevo: Buscar información de ubicación en OpenStreetMap


@app.route('/location', methods=['POST'])
def get_location():
    data = request.json
    place = data.get('place', '')

    if not place:
        return jsonify({"error": "No se proporcionó ningún lugar."}), 400

    # Consultar la API de OpenStreetMap
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": place,
        "format": "json",
        "addressdetails": 1,  # Proporciona detalles de la dirección
        "limit": 1            # Limita la búsqueda al primer resultado
    }
    response = requests.get(url, params=params, headers={"User-Agent": "flask-ajax-example"})


    if response.status_code == 200 and response.json():
        location_data = response.json()[0]
        return jsonify({
            "name": location_data.get('display_name'),
            "lat": location_data.get('lat'),
            "lon": location_data.get('lon')
        })
    else:
        return jsonify({"error": "No se encontraron resultados para el lugar especificado."}), 404

if __name__ == '__main__':
    app.run(debug=True)
