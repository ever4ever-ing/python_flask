from app import app  # Importamos la app de la carpeta flask_app
from app.controllers import controlador  # Importamos el controlador de usuarios

if __name__ == "__main__":  # Ejecutamos la aplicación

    app.run(debug=True)
