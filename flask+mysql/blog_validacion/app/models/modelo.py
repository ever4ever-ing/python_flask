from app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATABASE = 'esquema_blog'

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO usuarios (nombre, email, password, created_at, updated_at) 
        VALUES (%(nombre)s, %(email)s, %(password)s, NOW(), NOW())
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0]) if result else None
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0]) if result else None

    @staticmethod
    def validar_usuario(usuario):
        is_valid = True
        if len(usuario['nombre']) <= 0:
            flash("El nombre no puede estar vacío.", "danger")
            is_valid = False
        else:
            if len(usuario['nombre']) < 2:
                flash("El nombre debe tener al menos 2 caracteres.", "danger")
                is_valid = False

        if len(usuario['apellido']) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "danger")
            is_valid = False
        if not EMAIL_REGEX.match(usuario['email']):
            flash("Email inválido.", "danger")
            is_valid = False

        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        data = {'email': usuario['email']}
        resultado = connectToMySQL(DATABASE).query_db(query, data)
        if len(resultado) > 0:
            flash("El email ya está registrado.", "danger")
            is_valid = False
        if len(usuario['password']) <= 0:
            flash("La contraseña no puede estar vacía.", "danger")
            is_valid = False
        else:
            if len(usuario['password']) < 8:
                flash("La contraseña debe tener al menos 8 caracteres.", "danger")
                is_valid = False
            else:
                if len(usuario['confirmPassword']) <= 0:
                    flash("La confirmación de la contraseña no puede estar vacía.", "danger")
                    is_valid = False
                else:
                    if (usuario['password'] != usuario['confirmPassword']):
                        flash("Las contraseñas no coinciden.", "danger")
                        is_valid = False
        return is_valid
        
class Publicacion:
    def __init__(self, data):
        self.id = data['id']
        self.contenido = data['contenido']
        self.usuario_id = data['usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.comentarios = []  # Lista vacía para cargar comentarios
        self.autor = data.get('autor')  # Incluimos el autor si está en los datos

    @classmethod
    def get_all(cls):
        query = """
        SELECT publicaciones.*, usuarios.nombre AS autor
        FROM publicaciones 
        JOIN usuarios ON publicaciones.usuario_id = usuarios.id 
        ORDER BY publicaciones.created_at DESC
        """
        results = connectToMySQL(DATABASE).query_db(query)
        publicaciones = []
        for pub in results:
            publicaciones.append(cls(pub))
        return publicaciones
    


    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO publicaciones (contenido, usuario_id, created_at, updated_at) 
        VALUES (%(contenido)s, %(usuario_id)s, NOW(), NOW())
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM publicaciones WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

class Comentario:
    def __init__(self, data):
        self.id = data['id']
        self.comentario = data['comentario']
        self.usuario_id = data['usuario_id']
        self.publicacion_id = data['publicacion_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.autor = data.get('autor')  # Incluimos el autor si está en los datos

    @classmethod
    def get_by_publicacion_id(cls, data):
        query = """
        SELECT comentarios.*, usuarios.nombre AS autor 
        FROM comentarios 
        JOIN usuarios ON comentarios.usuario_id = usuarios.id 
        WHERE publicacion_id = %(publicacion_id)s
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        comentarios = []
        for com in results:
            comentarios.append(cls(com))
        return comentarios

    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO comentarios (comentario, usuario_id, publicacion_id, created_at, updated_at) 
        VALUES (%(comentario)s, %(usuario_id)s, %(publicacion_id)s, NOW(), NOW())
        """
        return connectToMySQL(DATABASE).query_db(query, data)
