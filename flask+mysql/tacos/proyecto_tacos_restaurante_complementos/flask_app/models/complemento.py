from flask_app.config.mysqlconnection import connectToMySQL  # importamos desde config
from flask_app.models import taco  # Importamos la clase Taco
DATABASE = 'esquema_tacos_restaurante_complemento'


class Complemento:

    def __init__(self, data):
        self.id = data['id']
        self.nombre_complementos = data['nombre_complementos']
        # creamos una lista en caso de que queramos mostrar qué tacos están relacionadas con el complemento
        self.en_tacos = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO complementos (nombre_complemento) VALUES (%(nombre_complemento)s)"
        return connectToMySQL(DATABASE).query_db(query, datos)
    # Recibimos en un diccionario el id del complemento que queremos consultar
    # El método recupera un complemento específico con los tacos asociados a él

    @classmethod
    def get_complementos_y_tacos(cls, datos):
        query = "SELECT * FROM complementos LEFT JOIN complementos_en_tacos ON complementos_en_tacos.complemento_id = complementos.id LEFT JOIN tacos ON complementos_en_tacos.taco_id = tacos.id WHERE complementos.id = %(id)s;"
        # los resultados serán una lista de diccionarios con la información del complemento y los tacos adjuntos a cada fila
        resultados = connectToMySQL(DATABASE).query_db(query, datos)
        complemento = cls(resultados[0])
        for fila_en_db in resultados:
            # Ahora parseamos los datos del taco para generar instancias de Taco y agregarlas a la lista
            datos_taco = {
                "id": fila_en_db['tacos.id'],
                "tortilla": fila_en_db['tortilla'],
                "guiso": fila_en_db['guiso'],
                "salsa": fila_en_db['salsa'],
                "created_at": fila_en_db['tacos.created_at'],
                "updated_at": fila_en_db['tacos.updated_at'],
            }

            complemento.en_tacos.append(taco.Taco(datos_taco))

        return complemento

    @classmethod
    def get_complemento_por_taco(cls, datos):
        query = "SELECT complementos.nombre_complementos FROM complementos LEFT JOIN complementos_en_tacos ON complementos_en_tacos.complemento_id = complementos.id LEFT JOIN tacos ON complementos_en_tacos.taco_id = tacos.id WHERE tacos.id = %(id)s;"
        resultados = connectToMySQL(DATABASE).query_db(query, datos)
        if not resultados or len(resultados) == 0:
            return None
        else:
            return resultados[0]['nombre_complementos']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM complementos;"
        resultados = connectToMySQL(DATABASE).query_db(query)
        complementos = []
        for complemento in resultados:
            complementos.append(cls(complemento))
        return complementos

    @classmethod
    def asignar_complemento(cls, datos):
        query = "INSERT INTO complementos_en_tacos (complemento_id, taco_id) VALUES (%(complemento_id)s, %(taco_id)s);"
        return connectToMySQL(DATABASE).query_db(query, datos)
