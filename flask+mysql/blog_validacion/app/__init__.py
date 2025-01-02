from flask import Flask #Importación de Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__) #Crea instancia de Flask

app.secret_key = "clave"
bcrypt = Bcrypt(app)
