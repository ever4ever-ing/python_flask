from flask_app import app 

from flask_app.controllers import usuarios
if __name__=="__main__": #Ejecutamos la aplicación

    app.run(debug=True)