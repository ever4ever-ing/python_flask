from app.config.mysqlconnection import connectToMySQL

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
    def create(cls, data):
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


class Publicacion:
    def __init__(self, data):
        self.id = data['id']
        self.contenido = data['contenido']
        self.usuario_id = data['usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.comentarios = []  # Lista vacía para cargar comentarios

    @classmethod
    def get_all(cls):
        query = """
        SELECT publicaciones.*, usuarios.nombre 
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
