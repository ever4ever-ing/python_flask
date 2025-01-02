from flask_app import app
# Ruta para mostrar la tabla de pedidos
from flask_app.controllers import pedidos  # Importamos el controlador de usuarios


if __name__ == "__main__":
    app.run(debug=True)
