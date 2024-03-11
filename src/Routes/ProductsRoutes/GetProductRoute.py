from flask import Blueprint, jsonify
from src.Models.ProductsModel import Product
from src.Utils.Logger import Logger
import traceback


main = Blueprint('getProduct', __name__)


# Ruta encargada de obtener un producto por su id
@main.get('api/product/<int:product_id>')
def get_product(product_id):
    try:
        # Buscar el producto por su ID en la base de datos
        product = Product.query.get(product_id)

        # Si el producto no existe, delvolver un mensaje de error
        if not product:
            return jsonify({"message": "Product not found"}), 404
        
        # Delver los datos del producto en formato JSON
        return jsonify({
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "quantity": product.quantity,
            "supplier_id": product.supplier_id,
            "category_id": product.category_id
        }), 200

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error getting product. Please try again later"}), 500