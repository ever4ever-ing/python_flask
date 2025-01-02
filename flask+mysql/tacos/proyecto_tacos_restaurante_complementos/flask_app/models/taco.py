from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
DATABASE = 'esquema_tacos_restaurante_complemento'


class Taco:
    def __init__(self, data):
        self.id = data['id']
        self.tortilla = data['tortilla']
        self.guiso = data['guiso']
        self.salsa = data['salsa']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.restaurante_id = data['restaurante_id']
        self.complementos = []

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO tacos (tortilla, guiso, salsa, restaurante_id) VALUES(%(tortilla)s, %(guiso)s, %(salsa)s, %(restaurante_id)s);"
        return connectToMySQL(DATABASE).query_db(query, datos)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM tacos;"
        tacos_en_bd = connectToMySQL(DATABASE).query_db(query)
        tacos = []
        for taco in tacos_en_bd:
            tacos.append(cls(taco))
        return tacos

    @classmethod
    def get_one(cls, datos):
        query = "SELECT * FROM tacos WHERE id = %(id)s;"
        taco_en_db = connectToMySQL(DATABASE).query_db(query, datos)

        return cls(taco_en_db[0])

    @classmethod
    def update(cls, datos):
        query = "UPDATE tacos SET tortilla=%(tortilla)s, guiso=%(guiso)s, salsa=%(salsa)s, restaurante_id=%(restaurante_id)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, datos)

    @classmethod
    def delete(cls, datos):
        query = "DELETE FROM tacos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, datos)

    @staticmethod
    def validar_taco(taco):
        es_valido = True  # Asumimos que la información en válida
        # Si la cantidad de caracteres para el campo tortilla es menor a 3
        if len(taco['tortilla']) < 3:
            # Generamos el mensaje
            flash("La tortilla debe tener al menos 3 caracteres",'warning')
            es_valido = False  # El formulario deja de ser válido
        if len(taco['guiso']) < 3:
            flash("La guiso debe tener al menos 3 caracteres")
            es_valido = False
        if len(taco['salsa']) < 3:
            flash("La salsa debe tener al menos 3 caracteres")
            es_valido = False
        return es_valido  # Regresamos si es válido o no
