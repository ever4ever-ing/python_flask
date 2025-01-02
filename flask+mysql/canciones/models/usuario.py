# /app/models/usuario.py
from config.mysqlconnection import connectToMySQL
db_name = "esquema_canciones"
class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.email = data['email']
        self.contraseña = data['contrasena']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.mis_favoritas = []


    @classmethod
    def obtener_todos(cls):
        query = "SELECT * FROM usuarios;"
        return connectToMySQL(cls.db_name).query_db(query)
    
    @classmethod
    def obtener_favoritos(cls, usuario_id):
        query = """
        SELECT canciones.* 
        FROM favoritos
        JOIN canciones ON favoritos.cancion_id = canciones.id
        WHERE favoritos.usuario_id = %(usuario_id)s;
        """
        data = {'usuario_id': usuario_id}
        return connectToMySQL(cls.db_name).query_db(query, data)
