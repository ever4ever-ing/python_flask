from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Pedido:
    def __init__(self, data):
        self.id = data['id']
        self.nombre_cliente = data['nombre_cliente']
        self.cantidad = data['cantidad']
        self.relleno = data['relleno']
        self.fecha_creacion = data['fecha_creacion']

    @staticmethod
    def get_all():
        query = "SELECT * FROM pedidos;"
        return connectToMySQL('pedidos_db').query_db(query)

    @staticmethod
    def save(data):
        query = """
            INSERT INTO pedidos (nombre_cliente, cantidad, relleno)
            VALUES (%(nombre_cliente)s, %(cantidad)s, %(relleno)s);
        """
        return connectToMySQL('pedidos_db').query_db(query, data)

    @staticmethod
    def validar_pedido(pedido):
        es_valido = True  # Asumimos que la información en válida
        # Si la cantidad de caracteres para el campo tortilla es menor a 3
        if len(pedido['nombre_cliente']) < 3:
            # Generamos el mensaje
            flash("El nombre debe tener al menos 3 caracteres", 'warning')
            es_valido = False  # El formulario deja de ser válido

        if pedido['cantidad'] <= 0:
            flash("La cantidad debe ser mayor a 0", 'warning')
            es_valido = False
            
        return es_valido
        
            
