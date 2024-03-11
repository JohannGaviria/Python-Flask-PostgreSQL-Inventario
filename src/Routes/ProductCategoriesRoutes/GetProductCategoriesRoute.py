from flask import Blueprint, jsonify
from src.Auth.ValidateProductCategorieData import ProductCategorieForm
from src.Models.ProductCategoriesModel import ProductCategory
from src.Utils.Logger import Logger
import traceback


main = Blueprint('getProductCategories', __name__)


@main.get('api/productCategories')
def get_product_categories():
    try:
        # Consultar todas las categorias de productos en la base de datos
        product_categories = ProductCategory.query.all()

        if product_categories:
            # Crear una lista de diccionarios con la información de las categorias de los productos
            product_categories_list = [{
                'id': product_categorie.id,
                'name': product_categorie.name
            } for product_categorie in product_categories]

            # Devolver la lista de las categorias de los productos en formato JSON
            return jsonify({"products categories": product_categories_list}), 200

        return jsonify({"message": "Product categories not founds"}), 404

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error getting product categories. Please try again later"}), 500