from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'esquema_estudiantes_cursos'
class Estudiante:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.curso_id = data['curso_id']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM estudiantes;"
        resultado = connectToMySQL(DATABASE).query_db(query)
        estudiantes=[]
        for estudiante in resultado:
            estudiante.append(cls(estudiante))
        return estudiantes
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO estudiantes (nombre, apellido, edad, curso_id) VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(curso_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    