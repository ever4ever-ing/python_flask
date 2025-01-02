from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key =   'mysecretkey'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adivina', methods=['POST'])
def adivina():
    print(request.form)
    session['nombre'] = request.form['nombre']  
    session['lugar'] = request.form['lugar']
    session['comida'] = request.form['comida']
    session['numero'] = request.form['numero']
    return redirect(url_for('futuro'))

@app.route('/futuro')
def futuro():
    return render_template('futuro.html', nombre=session['nombre'], lugar=session['lugar'], comida=session['comida'], numero=session['numero'])


if __name__ == '__main__':
    app.run(debug=True)
