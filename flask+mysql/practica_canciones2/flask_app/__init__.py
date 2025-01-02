from flask import Flask

app = Flask(__name__) ##creacion de instancia de clase

app.secret_key = '123456'