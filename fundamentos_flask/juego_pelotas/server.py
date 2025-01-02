from flask import Flask, render_template

app = Flask(__name__)

@app.route('/juego')
def home():
    return render_template('index.html', pelotas=3)

@app.route('/juego/<int:pelotas>')
def numero_pelotas(pelotas):
    return render_template('index.html', pelotas=pelotas)

@app.route('/juego/<int:pelotas>/<color>')
def color_pelotas(pelotas, color):
    return render_template('index.html', pelotas=pelotas,
                            color_pelota=color)

if __name__ == '__main__':
    app.run(debug=True)