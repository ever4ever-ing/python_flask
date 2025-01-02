# app.py
from flask import Flask, render_template
import random

app = Flask(__name__)

# Lista de colores y cartas
COLORS = ['pink', '#1E90FF', 'yellow']
CARDS = [
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
@app.route('/loteria')
@app.route('/loteria/<int:rows>/<int:cols>')
def loteria(rows=4, cols=3):
    # Genera un patrón de colores y cartas aleatorias para cada celda
    grid = []
    # Hacer una copia de las cartas para no repetir
    available_cards = CARDS.copy()
    
    for i in range(rows):
        row = []
        for j in range(cols):
            # Obtener color y carta aleatoria
            color_index = (i + j) % len(COLORS)
            card = random.choice(available_cards)
            # Remover la carta usada para evitar repeticiones
            available_cards.remove(card)
            
            # Crear diccionario con la información de la celda
            cell = {
                'color': COLORS[color_index],
                'card': card,
                'number': card.split()[0],
                'name': ' '.join(card.split()[1:])
            }
            row.append(cell)
        grid.append(row)
    
    return render_template('loteria.html', grid=grid, rows=rows, cols=cols)

if __name__ == '__main__':
    app.run(debug=True)