from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.estudiante import Estudiante
from flask_app.models.curso import Curso

@app.route('/nuevo_estudiante')
def nuevo_estudiante():
    todos_cursos = Curso.get_all()
    return render_template("nuevo_estudiante.html", todos_cursos=todos_cursos)


@app.route('/crear',methods=['POST'])
def crear_estudiante():
    datos = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "edad": request.form['edad'],
        "curso_id": request.form['curso_id']
    }
    Estudiante.save(datos)
    return redirect('/cursos')
