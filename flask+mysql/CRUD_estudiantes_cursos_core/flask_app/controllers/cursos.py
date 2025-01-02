from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.curso import Curso
from flask import flash


@app.route('/cursos')
def cursos():
    cursos = Curso.get_all()#llama a la capa modelo y obtiene una lista de cursos
    return render_template("cursos.html", cursos=cursos)


@app.route('/nuevo_crear', methods=['POST'])
def crear_curso():
    datos = {
        "nombre": request.form['nombre']
    }
    print("controller")
    print(datos)
    Curso.save(datos)
    return redirect('/cursos')


@app.route('/cursos/<int:id>') #ruta dinamica
def curso(id):
    datos = {
        "id": id
    }
    curso = Curso.get_cursos_estudiante(datos)
    if not curso:
        flash("No existe el curso")
        return redirect('/cursos')
    return render_template("estudiantes.html", curso=curso)


