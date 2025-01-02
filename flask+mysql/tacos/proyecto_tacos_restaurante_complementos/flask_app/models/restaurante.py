from flask_app.models import taco #Importamos la clase Taco
from flask_app.config.mysqlconnection import connectToMySQL #Importamos la función connectToMySQL
DATABASE = 'esquema_tacos_restaurante_complemento' #Nombre de la base de datos
class Restaurante:
    def __init__(self, data):
        self.id = int(data['id'])
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.tacos = [] # Lista de instancias de Taco
        #Ya que un restaurante puede tener muchos tacos asociados.

    @classmethod
    def get_restaurante_y_tacos(cls, datos):
        query = "SELECT * FROM restaurantes LEFT JOIN tacos ON tacos.restaurante_id = restaurantes.id WHERE restaurantes.id = %(id)s;"
        resultados = connectToMySQL(DATABASE).query_db(query, datos) #Consulta a la base de datos
        restaurante = cls(resultados[0])  # Creamos una instancia de Restaurante con los datos del restaurante
        for fila_en_db in resultados:
            if fila_en_db['tacos.id'] is not None:
                datos_taco = {
                    "id": fila_en_db['tacos.id'],
                    "tortilla": fila_en_db['tortilla'],
                    "guiso": fila_en_db['guiso'],
                    "salsa": fila_en_db['salsa'],
                    "created_at": fila_en_db['tacos.created_at'],
                    "updated_at": fila_en_db['tacos.updated_at'],
                    "restaurante_id": fila_en_db['restaurante_id']
                }
                # Agregando un nuevo taco a la lista de tacos del restaurante
                restaurante.tacos.append(taco.Taco(datos_taco)) 

        return restaurante
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM restaurantes;"
        resultados = connectToMySQL(DATABASE).query_db(query)
        restaurantes = []
        for restaurante in resultados:
            restaurantes.append(cls(restaurante) )
        return restaurantes
