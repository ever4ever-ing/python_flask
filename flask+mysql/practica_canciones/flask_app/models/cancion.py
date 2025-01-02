from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'esquema_canciones'

class Canciones:
    def __init__(self, data):
        self.id = data['id']
        self.titulo = data['titulo']
        self.artista = data['artista']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuarios_favoritos = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM canciones;"
        resultados = connectToMySQL(DATABASE).query_db(query)
        canciones = []
        for cancion in resultados:
            canciones.append(cls(cancion))
        return canciones
    
    @classmethod
    def agregar_cancion(cls, data):
            query = """INSERT INTO canciones (titulo, artista, created_at, updated_at)
            VALUES (%(titulo)s, %(artista)s, NOW(), NOW());"""
            return connectToMySQL(DATABASE).query_db(query, data)
    
    #Este método se utiliza para asignar los usuarios que han 
    #marcado una canción como favorita
    def assign_users(self):
        datos = {'cancion_id': self.id}
        self.usuarios_favoritos = Canciones.get_users_who_favorited(datos)

    #Este método estático se utiliza para obtener los usuarios que han
    # marcado una canción como favorita
    @classmethod
    def get_users_who_favorited(cls, datos):
        query = """SELECT usuarios.id, usuarios.nombre 
                FROM usuarios 
                JOIN favoritos ON usuarios.id = favoritos.usuario_id 
                WHERE favoritos.cancion_id = %(cancion_id)s;"""
        resultados = connectToMySQL(DATABASE).query_db(query, datos)
        return resultados
    
    @classmethod
    def get_by_id(cls, cancion_id):
        query = "SELECT * FROM canciones WHERE id = %(id)s;"
        datos = {'id': cancion_id}
        resultado = connectToMySQL(DATABASE).query_db(query, datos)
        if resultado:
            return cls(resultado[0])#nos quedamos con el primer elemento de la lista
        return None
    
    