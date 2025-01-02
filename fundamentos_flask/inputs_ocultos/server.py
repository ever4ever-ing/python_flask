from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = 'mysecretkey'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    if request.form['tipo_usuario'] == 'administrador':
        print('Proceso de un administrador')

    elif request.form['tipo_usuario'] == 'usuario':
        print('Proceso de un usuario')
    return redirect('/')

if __name__ == '__main__':
    app.run( debug=True)