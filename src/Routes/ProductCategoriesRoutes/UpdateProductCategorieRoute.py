from flask import Blueprint, jsonify, request
from src.Auth.ValidateProductCategorieData import ProductCategorieForm
from src.Models.ProductCategoriesModel import ProductCategory
from src.Utils.Database import db
from src.Utils.Logger import Logger
import traceback


main = Blueprint('uptadeProductCategorie', __name__)


@main.put('api/productCategorie/<int:product_categorie_id>')
def update_product_categorie(product_categorie_id):
    try:
        # Obtener los datos en formato JSON enviados en la solicitud
        data = request.get_json()

        # Validar los datos del producto
        form = ProductCategorieForm(data=data)

        # Si los datos son validos
        if form.validate():
            # Extraer los datos
            name = form.name.data

            # Buscar la categoria del producto por su ID en la base de datos
            product_categorie = ProductCategory.query.get(product_categorie_id)

            # Si la categoria del producto no existe, devolver un mensaje de error
            if not product_categorie:
                return jsonify({"message": "Product categorie not found"}), 404
            
            # Actualizar los datos de la categoria del producto si se proporcionan en la solicitud
            if name:
                product_categorie.name = name
            
            with db.session() as session:
                # Guardar los cambios en la base de datos
                session.commit()
            
            # Devolver mensaje de exitos junto con los datos actualizados de la categoria del producto
                return jsonify({"message": "Product categorie updated successfully",
                                "product": {
                                    "id": product_categorie.id,
                                    "name": product_categorie.name
                                }}), 200
        
        # Si los datos no son validos
        else:
            # Obtener los errors de validación
            errors = form.errors
            return jsonify({"message": "Validation error", "errors": errors}), 400

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error updating product categorie. Please try again later"}), 500