from flask import Blueprint, jsonify
from src.Models.ProductsModel import Product
from src.Utils.Logger import Logger
import traceback


main = Blueprint('getProducts', __name__)


# Ruta encargada de obtener los productos
@main.get('api/products')
def get_products():
    try:
        # Consultar todos los productos en la base de datos
        products = Product.query.all()

        # Si existe algun registro de productos
        if products:
            # Crear una lista de diccionarios con la información de los productos
            products_list = [{
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'quantity': product.quantity,
                'supplier_id': product.supplier_id,
                'category_id': product.category_id
            } for product in products]

            # Devolver la lista de los productos en formato JSON
            return jsonify({"products": products_list}), 200

        return jsonify({"message": "Products not founds"}), 404

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error getting products. Please try again later"}), 500