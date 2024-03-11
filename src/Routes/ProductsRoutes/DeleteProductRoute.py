from flask import Blueprint, jsonify
from src.Models.ProductsModel import Product
from src.Utils.Database import db
from src.Utils.Logger import Logger
import traceback


main = Blueprint('deleteProduct', __name__)


# Ruta encargada de eliminar los productos
@main.delete('api/product/<int:product_id>')
def delete_product(product_id):
    try:
        # Buscar el producto por su ID en la base de datos
        product = Product.query.get(product_id)
        
        # Si el poducto no existe, devolver un mensaje de error
        if not product:
            return jsonify({"message": "Product not found"}), 404
        
        with db.session() as session:
            # Eliminar el producto de la base de datos
            session.delete(product)
            session.commit()
        
        # Devolver un mensaje de éxito
        return jsonify({"message": "Product deleted successfully"}), 200

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error deleting product. Please try again later"}), 500