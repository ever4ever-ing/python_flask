from flask_app.models import taco #Importamos la clase Taco
from flask_app.config.mysqlconnection import connectToMySQL #Importamos la función connectToMySQL

class Restaurante:
    def __init__(self, data):
        self.id = int(data['id'])
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.tacos = [] # Lista de instancias de Taco

    @classmethod
    def get_restaurante_y_tacos(cls, datos):
        query = "SELECT * FROM restaurantes LEFT JOIN tacos ON tacos.restaurante_id = restaurantes.id WHERE restaurantes.id = %(id)s;"
        resultados = connectToMySQL('esquema_tacos').query_db(query, datos)
        restaurante = cls(resultados[0])  # Pass the entire dictionary to the constructor
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
                restaurante.tacos.append(taco.Taco(datos_taco))
        return restaurante
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM restaurantes;"
        resultados = connectToMySQL('esquema_tacos').query_db(query)
        restaurantes = []
        for fila_en_db in resultados:
            restaurante = cls(fila_en_db)  # Pass the entire dictionary to the constructor
            restaurantes.append(restaurante)
        return restaurantes
