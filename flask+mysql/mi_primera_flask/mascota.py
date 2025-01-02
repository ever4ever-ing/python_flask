# Importamos la función que devolverá una instancia de una conexión
from mysqlconnection import connectToMySQL

# Creamos la clase basada en la tabla de mascotas
DATABASE = 'primera_flask'  # Nombre de la base de datos

class Mascota:

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.tipo = data['tipo']
        self.color = data['color']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Creamos un método de clase para consultar nuestra base de datos
    @classmethod # Este decorador le dice a Python que el siguiente método es un método de clase
    def get_all(cls): # cls es la convención para el primer argumento de un método de clase
        query = "SELECT * FROM mascotas;"  # Creamos una consulta para seleccionar todas las columnas de la tabla mascotas
        # Llamamos a función connectToMySQL con el esquema al que te diriges
        resultados = connectToMySQL(DATABASE).query_db(query)
        # Creamos una lista vacía para agregar nuestras instancias de mascota
        mascotas = []
        # Iteramos sobre los resultados de la base de datos y crear instancias de mascota con cls
        for mascota in resultados:
            mascotas.append(cls(mascota))
        return mascotas
    
    @classmethod
    def save(cls, datos):
        query = "INSERT INTO mascotas (nombre, tipo, color, created_at, updated_at) VALUES (%(nombre)s, %(tipo)s, %(color)s, NOW(), NOW());"
        return connectToMySQL('primera_flask').query_db(query, datos)
