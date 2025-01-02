from app import app 
from flask import Flask, render_template, request, redirect, session, flash
from app.models.modelo import Usuario, Publicacion, Comentario
from app import app, bcrypt

@app.route('/')
def login_registro():
    return render_template('login.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    data = {
        "nombre": request.form['nombre'],
        "email": request.form['email'],
        "apellido": request.form['apellido'],
        "password": request.form['password'],
        "confirmPassword": request.form['confirmPassword']
    }
    if not Usuario.validar_usuario(data):#crear metodo validar_usuario en el modelo
        return redirect('/')
    else:
        #cuando el usuario es valido
        pw_hash = bcrypt.generate_password_hash(request.form['password']) #Agregar bcrypt
        data = {
        "nombre": request.form['nombre'],
        "email": request.form['email'],
        "apellido": request.form['apellido'],
        "password": pw_hash
        }
        Usuario.save(data)
        return redirect('/')

@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    data= {"email": request.form['email']}
    usuario = Usuario.get_by_email(data)
    if not usuario :
        flash("Email no registrado")
        return redirect('/')
    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("Contraseña incorrecta")
        return redirect('/')
    
    session['usuario_id'] = usuario.id
    return redirect('/publicaciones')

@app.route('/publicaciones')
def publicaciones():
    if 'usuario_id' not in session:
        return redirect('/')
    publicaciones = Publicacion.get_all() #lista de publicaciones
    for pub in publicaciones:
        pub.comentarios = Comentario.get_by_publicacion_id({"publicacion_id": pub.id}) # Obtiene lISTA de comentarios de cada publicación
        autor = Usuario.get_by_id({"id": pub.usuario_id}) # Obtiene el usuario de cada publicación
        pub.autor = autor.nombre  # Accede al campo nombre del objeto autor y lo asigna a la publicación
    return render_template('publicaciones.html', publicaciones=publicaciones)

@app.route('/publicar', methods=['POST'])
def publicar():
    if 'usuario_id' not in session:
        return redirect('/')
    data = {
        "contenido": request.form['contenido'],
        "usuario_id": session['usuario_id']
    }
    Publicacion.create(data)
    return redirect('/publicaciones')

@app.route('/eliminar/<int:id>')
def eliminar(id):
    if 'usuario_id' not in session:
        return redirect('/')
    data = {"id": id}
    Publicacion.delete(data)
    return redirect('/publicaciones')

@app.route('/comentario', methods=['POST'])
def agregar_comentario():
    if 'usuario_id' not in session:
        return redirect('/')
    comentario = request.form['comentario'].strip()
    print(f"Comentario recibido: '{comentario}'")  # Debugging statement
    if not comentario:
        flash("El comentario no puede estar vacío")
        return redirect('/publicaciones')
    data = {
        "comentario": comentario,
        "usuario_id": session['usuario_id'],
        "publicacion_id": request.form['publicacion_id']
    }
    Comentario.create(data)
    return redirect('/publicaciones')

