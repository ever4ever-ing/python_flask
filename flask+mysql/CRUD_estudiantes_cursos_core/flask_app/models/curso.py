from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import estudiante
DATABASE = 'esquema_estudiantes_cursos'


class Curso:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.estudiantes = []

    @classmethod
    def get_all(cls):
        """
        Consulta a la base de datos para obtener todos los registros de la tabla 'cursos'.
        Retorna:
            list: Una lista de instancias de la clase 'Curso', cada una 
            representando un registro de la tabla 'cursos'.
        """
        query = "SELECT * FROM cursos;"
        resultado = connectToMySQL(DATABASE).query_db(query)
        cursos = []
        for curso in resultado:
            cursos.append(cls(curso))
        return cursos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO cursos (nombre, created_at, updated_at) VALUES (%(nombre)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_cursos_estudiante(cls, datos):
        query = "SELECT * FROM cursos LEFT JOIN estudiantes ON estudiantes.curso_id = cursos.id WHERE cursos.id = %(id)s;"
        resultados = connectToMySQL(DATABASE).query_db(
            query, datos)  # Consulta a la base de datos
        print("***Resultado:", len(resultados))
        if len(resultados) == 0:
            return None  # O cualquier valor que desees retornar en caso de que no haya resultados
        else:
            curso = cls(resultados[0])  # Creamos una instancia de Curso
            for fila_en_db in resultados:
                if fila_en_db['estudiantes.id'] is not None:
                    datos_estudiante = {
                        "id": fila_en_db['estudiantes.id'],
                        "nombre": fila_en_db['estudiantes.nombre'],
                        "apellido": fila_en_db['apellido'],
                        "edad": fila_en_db['edad'],
                        "created_at": fila_en_db['created_at'],
                        "updated_at": fila_en_db['updated_at'],
                        "curso_id": fila_en_db['id']
                    }
                    # Agregando un nuevo taco a la lista de tacos del restaurante
                    curso.estudiantes.append(
                        estudiante.Estudiante(datos_estudiante))
            return curso
