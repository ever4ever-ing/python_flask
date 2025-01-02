from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = 'esquema_seguidores'
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
        return cls(result[0]) if result else None # Si no hay resultados, regresamos None
    
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

    @classmethod
    def get_user_with_followers(cls, id):
        query = """
        SELECT usuarios.*, seguidores.id_seguidor, seguidor.nombre AS seguidor_nombre, seguidor.apellido AS seguidor_apellido
        FROM usuarios
        LEFT JOIN seguidores ON usuarios.id = seguidores.id_usuario
        LEFT JOIN usuarios AS seguidor ON seguidores.id_seguidor = seguidor.id
        WHERE usuarios.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, {'id': id})
        if not results:
            return None
        
        user = cls(results[0])
        user.followers = []
        for row in results:
            if row['id_seguidor']:
                follower_data = {
                    'id': row['id_seguidor'],
                    'nombre': row['seguidor_nombre'],
                    'apellido': row['seguidor_apellido'],
                    'email': None,
                    'created_at': None,
                    'updated_at': None
                }
                user.followers.append(cls(follower_data))
        return user
