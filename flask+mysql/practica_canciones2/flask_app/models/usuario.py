# Nos podemos conectar a la BD y podemos jugar con la creacion del objeto y sus metodos
from flask_app.config.mysqlconnection import connectToMySQL
# aqui debes importar otras clases en caso de que sea necesario

DATABASE = 'esquema_canciones'


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
    def get_all(cls):
        # Este método se encarga de traer todos los usuarios de la base de datos
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL(DATABASE).query_db(query)
        usuarios = []
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios

    @classmethod
    def get_all_users(cls):
        query = "SELECT id, nombre FROM usuarios;"
        resultados = connectToMySQL(DATABASE).query_db(query)
        return resultados

    @classmethod
    def get_canciones_y_usuarios(cls, datos):
        query = """SELECT canciones.id AS cancion_id, canciones.titulo, canciones.artista, canciones.created_at AS cancion_created_at, canciones.updated_at AS cancion_updated_at, 
                    usuarios.id AS usuario_id, usuarios.nombre, usuarios.email, usuarios.contrasena, usuarios.created_at AS usuario_created_at, usuarios.updated_at AS usuario_updated_at 
                    FROM canciones 
                    LEFT JOIN favoritos ON favoritos.cancion_id = canciones.id 
                    LEFT JOIN usuarios ON favoritos.usuario_id = usuarios.id 
                    WHERE usuarios.id = %(id)s;"""
        resultados = connectToMySQL('esquema_canciones').query_db(query, datos)

        if len(resultados) == 0:
            return None
        # Para obtener los datos del usuario basta con obtener la primera fila de resultados
        usuario_data = {
            'id': resultados[0]['usuario_id'],
            'nombre': resultados[0]['nombre'],
            'email': resultados[0]['email'],
            'contrasena': resultados[0]['contrasena'],
            'created_at': resultados[0]['usuario_created_at'],
            'updated_at': resultados[0]['usuario_updated_at']
        }
        # Creamos una instancia de Usuario con los datos obtenidos
        usuario = Usuario(usuario_data)

        for fila_en_db in resultados:
            datos_cancion = {
                'id': fila_en_db['cancion_id'],
                'titulo': fila_en_db['titulo'],
                'artista': fila_en_db['artista'],
                'created_at': fila_en_db['cancion_created_at'],
                'updated_at': fila_en_db['cancion_updated_at']
            }
            usuario.mis_favoritas.append(datos_cancion)

        return usuario

    @classmethod
    def get_canciones_y_usuarios_simplificado(cls, datos):
        query = """SELECT canciones.id AS cancion_id, canciones.titulo, canciones.artista, canciones.created_at AS cancion_created_at, canciones.updated_at AS cancion_updated_at, 
                    usuarios.id AS usuario_id, usuarios.nombre, usuarios.email, usuarios.contrasena, usuarios.created_at AS usuario_created_at, usuarios.updated_at AS usuario_updated_at 
                    FROM canciones 
                    LEFT JOIN favoritos ON favoritos.cancion_id = canciones.id 
                    LEFT JOIN usuarios ON favoritos.usuario_id = usuarios.id 
                    WHERE usuarios.id = %(id)s;"""
        resultados = connectToMySQL('esquema_canciones').query_db(query, datos)
        return resultados
    
    
    #core Recupera todas las canciones que un usuario marcó como favoritas
    @classmethod
    def get_favoritas(cls, datos):
        query = """SELECT canciones.id, canciones.titulo, canciones.artista 
                FROM canciones
                JOIN favoritos ON canciones.id = favoritos.cancion_id
                JOIN usuarios ON usuarios.id = favoritos.usuario_id
                WHERE usuarios.id = %(id)s;"""
        resultados = connectToMySQL(DATABASE).query_db(query, datos)
        return resultados
