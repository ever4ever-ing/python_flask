from flask_app.config.mysqlconnection import connectToMySQL ###Nos podemos conectar a la BD y podemos jugar con la creacion del objeto y sus metodos
#####aqui debes importar otras clases en caso de que sea necesario


class Ejemplo1:
    db_schema = 'ejemplos1' ## Cambiar la BD a la que estamos apuntando
    def __init__(self,data):
        self.id = data['id'] 
# Agregar el reto de atributos que vienen de la Base de datos

    @classmethod
    def get_all(cls):
        query = "select * from ejemplos1;" ###cambiar la tabla a la que apuntamos.
        resultados = connectToMySQL(cls.db_schema).query_db(query)
        ejemplos1 = [] ###Cambiar el nombre del arreglo para algo que represente la tabla
        for ejemplo1 in resultados:
            ejemplos1.append(cls(ejemplo1))
        return ejemplos1
