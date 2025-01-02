from flask import Flask, render_template, request, redirect, url_for, session #importar librerias

app = Flask(__name__) #instanciar aplicacion
app.secret_key = 'mysecret' #clave secreta

@app.route('/', methods=['GET'])
def home():
    #comprobar que el usuario no haya visitado la pagina
    if 'visitas' not in session:
        session['visitas'] = 0 #parto en cero
        session['visitas'] += 1 #incremento en uno
    else:
        session['visitas'] += 1 #incremento en uno
    return render_template('index.html', visitas=session['visitas']) #renderizar la plantilla

@app.route('/destruir_sesion', methods=['POST'])
def destruir_sesion():
    session.clear()
    return redirect(url_for('home'))

@app.route('/aumentar_dos', methods=['POST'])
def aumentar_dos():
    session['visitas'] += 1
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True) #correr aplicacion

#session.clear() #limpiar sesion