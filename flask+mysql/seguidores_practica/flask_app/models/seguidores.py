from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = 'esquema_seguidores'
class Seguidores:
    def __init__(self, data):
        self.id = data['id']
        self.usuario_id = data['usuario_id']
        self.seguidor_id = data['seguidor_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    #obtener todos los seguidores
    @classmethod
    def get_all_followers(cls, usuario_id):
        pass
    #obtener los seguidores de un usuario
    @classmethod
    def get_user_followers(cls, usuario_id):
        query = """
            SELECT u1.nombre AS nombre_usuario, u1.apellido AS apellido_usuario,
            u2.nombre AS nombre_seguidor, u2.apellido AS apellido_seguidor
            FROM usuarios u1
            INNER JOIN seguidores s ON u1.id = s.usuario_id
            LEFT JOIN usuarios u2 ON s.seguidor_id = u2.id
            WHERE u1.id = %(usuario_id)s;
            """
        data = {
            'usuario_id': usuario_id
        }
        results = connectToMySQL(DATABASE).query_db(query, data)
        user_followers = []
        for row in results:
                user_follower_data = {
                    'nombre_usuario': row['nombre_usuario'],
                    'apellido_usuario': row['apellido_usuario'],
                    'nombre_seguidor': row['nombre_seguidor'],
                    'apellido_seguidor': row['apellido_seguidor']
                }
                user_followers.append(user_follower_data)
        return user_followers
    #Agregar un seguidor
    @classmethod
    def add_follower(cls, data):
        query = "INSERT INTO seguidores (usuario_id, seguidor_id) VALUES (%(usuario_id)s, %(seguidor_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)