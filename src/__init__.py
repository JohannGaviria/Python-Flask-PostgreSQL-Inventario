from flask import Flask
from .Routes import IndexRoute


# Inicializamos la aplicación flask
app = Flask(__name__)


# Función para inicializar la aplicación con la configuración proporcionada 
def init_app(config):
    app.config.from_object(config) # Configuramos la aplicación con el objecto de configuración

    # Registramos todas las rutas
    app.register_blueprint(IndexRoute.main, url_prefix='/')

    return app # Retonarmos la aplicación inicializada