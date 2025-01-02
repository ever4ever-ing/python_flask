from flask import render_template, request, redirect
from flask_app.models.usuario import Usuario
from flask_app.models.seguidores import Seguidores
from flask_app import app

@app.route('/')
def index():
    users = Usuario.get_all()
    #followers = Seguidores.get_all_followers(usuario_id=1)
    user_followers = Seguidores.get_user_followers(usuario_id=1)
    print(user_followers)
    return render_template('index.html', users=users, followers=user_followers)


@app.route('/follow_user', methods=['POST'])
def follow_user():
    usuario_id = request.form['usuario_id']
    seguidor_id = request.form['seguidor_id']
    data = {
        'usuario_id': usuario_id,
        'seguidor_id': seguidor_id
    }
    Seguidores.add_follower(data)
    return redirect('/')