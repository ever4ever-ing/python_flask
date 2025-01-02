from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    fresa = request.form['fresa']
    manzana = request.form['manzana']
    frambuesa = request.form['frambuesa']
    print(f"fresa: {fresa}, manzana: {manzana}, frambuesa: {frambuesa}")
    print(f"Total: {int(fresa) + int(manzana) + int(frambuesa)}")
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']

    return render_template("checkout.html", fresa=fresa, manzana=manzana, frambuesa=frambuesa, nombre=nombre, apellido=apellido, email=email)


@app.route('/frutas')
def fruits():
    return render_template("frutas.html")


if __name__ == "__main__":
    app.run(debug=True)
