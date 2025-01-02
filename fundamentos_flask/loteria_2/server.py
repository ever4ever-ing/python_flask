from flask import Flask, render_template, request, redirect, url_for, session,flash
import random

app = Flask(__name__)
app.secret_key = 'secret'
cartas = [
    "1  El Gallo", "2  El Diablito", "3  La Dama", "4  El catrín", "5  El paraguas",
    "6  La sirena", "7  La escalera", "8  La botella", "9  El barril", "10 El árbol",
    "11 El melón", "12 El valiente", "13 El gorrito", "14 La muerte", "15 La pera",
    "16 La bandera", "17 El bandolón", "18 El violoncello", "19 La garza", "20 El pájaro",
    "21 La mano", "22 La bota", "23 La luna", "24 El cotorro", "25 El borracho",
    "26 El negrito", "27 El corazón", "28 La sandía", "29 El tambor", "30 El camarón",
    "31 Las jaras", "32 El músico", "33 La araña", "34 El soldado", "35 La estrella",
    "36 El cazo", "37 El mundo", "38 El apache", "39 El nopal", "40 El alacrán",
    "41 La rosa", "42 La calavera", "43 La campana", "44 El cantarito", "45 El venado",
    "46 El sol", "47 La corona", "48 La chalupa", "49 El pino", "50 El pescado",
    "51 La palma", "52 La maceta", "53 El arpa", "54 La rana"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adivina', methods=['POST'])
def adivina():

    carta = random.choice(cartas)
    seleccionada = carta.split()[0]
    session['seleccionada'] = seleccionada
    print('Carta seleccionada: ')
    print(session['seleccionada'])

    if 'intento' not in session:
        session['intento'] = 0 #parto en cero
        session['intento'] += 1 #incremento en uno
    elif session['intento'] == 3:
        print('Se acabaron los intentos')
        session['estado'] = 'Perdiste'
        flash('Se acabaron los intentos')
    else:
        session['intento'] += 1 #incremento en uno

    session['numero'] = request.form['numero']
    
    if session['numero'] == session['seleccionada']:
        session['estado'] = 'Ganaste'
        flash('Ganaste')
    else:
        session['estado'] = 'Perdiste'
        flash('Perdiste')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)