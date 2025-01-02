from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

DATABASE = 'esquema_usuarios'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        # Este método se encarga de traer todos los usuarios de la base de datos
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL(DATABASE).query_db(query)
        usuarios = []
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, {'id': id})
        # Si no hay resultados, regresamos None
        return cls(result[0]) if result else None

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, datos)

    @classmethod
    def update(cls, datos):
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, datos)

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, {'id': id})

    @staticmethod #metodo estatico no modifica la clase, no necesita self, cls
    def validar_usuario(usuario):
        es_valido = True
        #Revisa si el campo coincide con el patrón
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        data = {'email': usuario['email']}
        resultado = connectToMySQL(DATABASE).query_db(query, data)
        if len(usuario['nombre'])<=0:
            flash("El campo nombre es obligatorio", "secondary")
            es_valido = False
            return es_valido
        if len(usuario['apellido'])<=0:
            flash("El campo apellido es obligatorio", "secondary")
            es_valido = False
            return es_valido
        if len(usuario['email'])<=0:
            flash("El campo email es obligatorio", "secondary")
            es_valido = False
            return es_valido
        if not EMAIL_REGEX.match(usuario['email']):
            flash("E-mail inválido", "secondary")
            es_valido = False
            return es_valido
        elif len(resultado) > 0:
            flash("E-mail ya registrado", "secondary")
            es_valido = False
            return es_valido
        else:
            flash('Usuarios registrado exitosamente', "success")
            return es_valido
        
    
