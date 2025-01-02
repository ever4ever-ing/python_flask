from flask_app import app #Importamos la app de la carpeta flask_app
from flask_app.controllers import tacos, restaurantes #Importamos los controladores de tacos y restaurantes
from flask import render_template #Importamos la función render_template
from flask_app.models.restaurante import Restaurante #Importamos la clase Restaurante
from flask_app.models.complemento import Complemento #Importamos la clase Complemento

@app.route('/')
def index():
    todos_restaurantes = Restaurante.get_all()
    todos_complementos = Complemento.get_all()
    return render_template("index.html", todos_restaurantes=todos_restaurantes, todos_complementos=todos_complementos)  # todos_restaurantes is passed to the template

if __name__=="__main__": #Ejecutamos la aplicación

    app.run(debug=True)