from flask import Blueprint, jsonify, request
from src.Auth.ValidateProductCategorieData import ProductCategorieForm
from src.Models.ProductCategoriesModel import ProductCategory
from src.Utils.Database import db
from src.Utils.Logger import Logger
import traceback


main = Blueprint('deleteProductCategorie', __name__)


# Ruta encargada de eliminar a las categorias de los productos
@main.delete('api/productCategorie/<int:product_categorie_id>')
def delete_product_categorie(product_categorie_id):
    try:
        # Buscar la categoria del producto por su ID en la base de datos
        product_categorie = ProductCategory.query.get(product_categorie_id)
        
        # Si la categoria del poducto no existe, devolver un mensaje de error
        if not product_categorie:
            return jsonify({"message": "Product categorie not found"}), 404
        
        with db.session() as session:
            # Eliminar la categoria del producto de la base de datos
            session.delete(product_categorie)
            session.commit()
        
        # Devolver un mensaje de éxito
        return jsonify({"message": "Product categorie deleted successfully"}), 200

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error deleting product categorie. Please try again later"}), 500