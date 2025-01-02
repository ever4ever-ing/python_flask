# Errores

## Errores posibles

### 1. Error de autenticacion
OperationalError
pymysql.err.OperationalError: (1045, "Access denied for user 'root'@'localhost' (using password: YES)")
#### Revisar los datos de autenticacion en el archivo `mysqlconnection.py`
- usuario
- password

### 2. Error de conexion a la base de datos

OperationalError
pymysql.err.OperationalError: (1049, "Unknown database 'nombre_de_base_de_datos'")
#### Revisar nombre de base de datos en archivo  `modelo.py` 


