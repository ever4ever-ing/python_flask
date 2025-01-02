from flask_app import app
from flask import render_template, redirect,request,session
from flask_app.models.ejemplo1 import Ejemplo1



@app.route('/')

def main():
    return render_template('index.html')


