from flask_app import app 
#importar los controladores que manejan las rutas
from flask_app.controllers import usuarios 
if __name__=="__main__": #Ejecutamos la aplicación
    app.run(debug=True)