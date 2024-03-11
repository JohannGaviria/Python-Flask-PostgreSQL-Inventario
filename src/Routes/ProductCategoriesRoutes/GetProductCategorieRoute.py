from flask import Blueprint, jsonify
from src.Auth.ValidateProductCategorieData import ProductCategorieForm
from src.Models.ProductCategoriesModel import ProductCategory
from src.Utils.Logger import Logger
import traceback


main = Blueprint('getProductCategorie', __name__)


# Ruta encargada de obtener una categoria de producto por su id
@main.get('api/productCategorie/<int:product_categorie_id>')
def get_product_categorie(product_categorie_id):
    try:
        # Buscar la categoria del producto por su ID en la base de datos
        product_categorie = ProductCategory.query.get(product_categorie_id)

        # Si la categoria del producto no existe, delvolver un mensaje de error
        if not product_categorie:
            return jsonify({"message": "Product categorie not found"}), 404
        
        # Delver los datos de la categoria del producto en formato JSON
        return jsonify({
            "id": product_categorie.id,
            "name": product_categorie.name
        }), 200

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error getting product categorie. Please try again later"}), 500