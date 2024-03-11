from flask import Blueprint, jsonify, request
from src.Auth.ValidateProductCategorieData import ProductCategorieForm
from src.Models.ProductCategoriesModel import ProductCategory
from src.Utils.Database import db
from src.Utils.Logger import Logger
import traceback


main = Blueprint('createProductCategorie', __name__)


# Ruta encargada de crear las categorias de los productos
@main.post('api/productCategorie')
def create_product_categorie():
    try:
        # Obtener los datos en formato JSON enviados en la solicitud
        data = request.get_json()

        # Validar los datos la categoria del producto
        form = ProductCategorieForm(data=data)

        # Si los datos son validos
        if form.validate():
            # Extraer los datos
            name = form.name.data

            with db.session() as session:
                # Guardar la nueva categoria del producto
                new_product_categorie = ProductCategory(name)
                session.add(new_product_categorie)
                session.commit()

                return jsonify({"message": "Product categorie created successfully"}), 200

        # Si los datos no son validos
        else:
            # Obtener los errores de validación
            errors = form.errors
            return jsonify({"message": "Validation error", "errors": errors}), 400

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error creating product categorie. Please try again later"}), 500