from flask import Blueprint, jsonify, request
from src.Auth.ValidateProductData import ProductForm
from src.Models.ProductsModel import Product
from src.Models.SuppliersModel import Supplier
from src.Models.ProductCategoriesModel import ProductCategory
from src.Utils.Database import db
from src.Utils.Logger import Logger
import traceback


main = Blueprint('createProduct', __name__)


# Ruta encargada de manejar la creación de los productos
@main.post('api/product')
def create_product():
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

            with db.session() as session:
                supplier = session.query(Supplier).get(supplier_id)
                product_category = session.query(Supplier).get(category_id)

                # Guardar el nuevo producto
                new_product = Product(name, description, price, quantity, supplier.id, product_category.id)
                session.add(new_product)
                session.commit()

                return jsonify({"message": "Product created successfully"}), 200
        
        # Si los datos no son validos
        else:
            # Obtener los errores de validación
            errors = form.errors
            return jsonify({"message": "Validation error", "errors": errors}), 400

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error creating product. Please try again later"}), 500
    

