from flask import Flask
from .Routes.SuppliersRoutes import CreateSupplierRoute, GetSupplierRoute, GetSuppliersRoute, UpdateSupplierRoute, DeleteSupplierRoute
from .Routes.ProductsRoutes import CreateProductRoute, GetProductRoute, GetProductsRoute, UpdateProductRoute, DeleteProductRoute
from .Routes.ProductCategoriesRoutes import CreateProductCategorieRoute, GetProductCategoriesRoute, GetProductCategorieRoute, UpdateProductCategorieRoute, DeleteProductCategorieRoute
from .Routes.MovementTypesRoutes import CreateMovementTypeRoute, GetMovementTypesRoute, GetMovementTypeRoute, DeleteMovementTypeRoute, UpdateMovementTypeRoute
from .Routes.InventoryMovementsRoutes import CreateInventoryMovementRoute, GetInventoryMovementsRoute, GetInventoryMovementRoute, DeleteInventoryMovementRoute, UpdateInventoryMovementRoute
from .Utils.Database import db
from dotenv import load_dotenv
from os import environ


# Cargamos las variables de entorno desde el archivo .env
load_dotenv()


# Inicializamos la aplicación flask
app = Flask(__name__)


# Función para inicializar la aplicación con la configuración proporcionada 
def init_app(config):
    app.config.from_object(config) # Configuramos la aplicación con el objecto de configuración

    # Configuracion de conexión a la base de datos de postgreSQL usando variables de entorno
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{environ.get('DB_USER')}:{environ.get('DB_PASSWORD')}@{environ.get('DB_HOST')}/{environ.get('DB_DATABASE')}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Desactivamos el seguimiento de modificaciones de SQLAlchemy

    db.init_app(app) # Inicializamos la base de datos con la aplicación

    app.config['WTF_CSRF_ENABLED'] = False # Desactivamos la proteción CRSF para simplificar la prueba de la API

    # Registramos todas las rutas
    app.register_blueprint(CreateSupplierRoute.main, url_prefix='/')
    app.register_blueprint(GetSuppliersRoute.main, url_prefix='/')
    app.register_blueprint(UpdateSupplierRoute.main, url_prefix='/')
    app.register_blueprint(GetSupplierRoute.main, url_prefix='/')
    app.register_blueprint(DeleteSupplierRoute.main, url_prefix='/')

    app.register_blueprint(CreateProductRoute.main, url_prefix='/')
    app.register_blueprint(GetProductsRoute.main, url_prefix='/')
    app.register_blueprint(GetProductRoute.main, url_prefix='/')
    app.register_blueprint(UpdateProductRoute.main, url_prefix='/')
    app.register_blueprint(DeleteProductRoute.main, url_prefix='/')

    app.register_blueprint(CreateProductCategorieRoute.main, url_prefix='/')
    app.register_blueprint(GetProductCategoriesRoute.main, url_prefix='/')
    app.register_blueprint(GetProductCategorieRoute.main, url_prefix='/')
    app.register_blueprint(UpdateProductCategorieRoute.main, url_prefix='/')
    app.register_blueprint(DeleteProductCategorieRoute.main, url_prefix='/')

    app.register_blueprint(CreateMovementTypeRoute.main, url_prefix='/')
    app.register_blueprint(GetMovementTypesRoute.main, url_prefix='/')
    app.register_blueprint(GetMovementTypeRoute.main, url_prefix='/')
    app.register_blueprint(DeleteMovementTypeRoute.main, url_prefix='/')
    app.register_blueprint(UpdateMovementTypeRoute.main, url_prefix='/')

    app.register_blueprint(CreateInventoryMovementRoute.main, url_prefix='/')
    app.register_blueprint(GetInventoryMovementsRoute.main, url_prefix='/')
    app.register_blueprint(GetInventoryMovementRoute.main, url_prefix='/')
    app.register_blueprint(UpdateInventoryMovementRoute.main, url_prefix='/')
    app.register_blueprint(DeleteInventoryMovementRoute.main, url_prefix='/')

    return app # Retonarmos la aplicación inicializada
