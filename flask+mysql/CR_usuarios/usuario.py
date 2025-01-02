# Importamos la función que devolverá una instancia de una conexión
from mysqlconnection import connectToMySQL

# Creamos la clase basada en la tabla de mascotas
DATABASE = 'esquema_usuarios'  # Nombre de la base de datos

class Usuario:

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Creamos un método de clase para consultar nuestra base de datos
    @classmethod # Este decorador le dice a Python que el siguiente método es un método de clase
    def get_all(cls): # cls es la convención para el primer argumento de un método de clase
        query = "SELECT * FROM usuarios;"  # Creamos una consulta para seleccionar todas las columnas de la tabla 
        # Llamamos a función connectToMySQL con el esquema al que te diriges
        resultados = connectToMySQL(DATABASE).query_db(query)
        # Creamos una lista vacía para agregar nuestras instancias 
        usuarios = []
        # Iteramos sobre los resultados de la base de datos y crear instancias con cls
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios
    
    @classmethod
    def save(cls, datos):
        query = "INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, datos)
