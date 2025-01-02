from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Obtener datos enviados por AJAX
    data = request.json
    name = data.get('name', '')

    # Respuesta personalizada
    if name:
        response = {"message": f"Hola, {name}!"}
    else:
        response = {"message": "Por favor, introduce un nombre."}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
