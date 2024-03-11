from flask import Blueprint, jsonify, request
from src.Auth.ValidateProductData import ProductForm
from src.Models.ProductsModel import Product
from src.Utils.Database import db
from src.Utils.Logger import Logger
import traceback


main = Blueprint('updateProduct', __name__)


# Ruta encargada de manejar las actualizaciones de los productos
@main.put('api/product/<int:product_id>')
def update_product(product_id):
    try:
        # Obtener los datos en formato JSON enviados en la solicitud
        data = request.get_json()

        # Validar los datos del producto
        form = ProductForm(data=data)

        # Si los datos son validos
        if form.validate():
            # Extraer los datos
            name = form.name.data
            description = form.description.data
            price = form.price.data
            quantity = form.quantity.data
            supplier_id = form.supplier_id.data
            category_id = form.category_id.data

            # Buscar el producto por su ID en la base de datos
            product = Product.query.get(product_id)

            # Si el producto no existe, devolver un mensaje de error
            if not product:
                return jsonify({"message": "Product not found"}), 404
            
            # Actualizar los datos del producto si se proporcionan en la solicitud
            if name:
                product.name = name
            if description:
                product.description = description
            if price:
                product.price = price
            if quantity:
                product.quantity = quantity
            if supplier_id:
                product.supplier_id = supplier_id
            if category_id:
                product.category_id = category_id

            with db.session() as session:
                # Guardar los cambios en la base de datos
                session.commit()
            
            # Devolver mensaje de exitos junto con los datos actualizados del producto
                return jsonify({"message": "Product updated successfully",
                                "product": {
                                    "id": product.id,
                                    "name": product.name,
                                    "description": product.description,
                                    "price": product.price,
                                    "quantity": product.quantity,
                                    "supplier_id": product.supplier_id,
                                    "category_id": product.category_id
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
        return jsonify({"message": "Error updating product. Please try again later"}), 500