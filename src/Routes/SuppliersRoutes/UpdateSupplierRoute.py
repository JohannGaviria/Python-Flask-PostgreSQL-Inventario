from flask import Blueprint, jsonify, request
from src.Auth.ValidateSupplierData import SupplierForm
from src.Models.SuppliersModel import Supplier
from src.Utils.Database import db
from src.Utils.Logger import Logger
import traceback


main = Blueprint('updateSupplier', __name__)


# Ruta encargada de manejar las actualizaciones de los proveedores
@main.put('api/supplier/<int:supplier_id>')
def update_supplier(supplier_id):
    try:
        # Obtener los datos en formato JSON enviados en la solicitud
        data = request.get_json()

        # Validar los datos del proveedor
        form = SupplierForm(data=data)

        # Si los datos son validos
        if form.validate():
            # Extraer los datos
            name = form.name.data
            address = form.address.data
            contact = form.contact.data

            # Buscar el proveedor por su ID en la base de datos
            supplier = Supplier.query.get(supplier_id)
            
            # Si el proveedor no existe, devolver un mensaje de error
            if not supplier:
                return jsonify({"message": "Supplier not found"}), 404
            
            # Actualizar los datos del proveedor si se proporcionan en la solicitud
            if name:
                supplier.name = name
            if address:
                supplier.address = address
            if contact:
                supplier.contact = contact
            
            with db.session() as session:
                # Guardar los cambios en la base de datos
                session.commit()
            
            # Devolver un mensaje de éxito junto con los datos actualizados del proveedor en formato JSON
            return jsonify({"message": "Supplier updated successfully",
                            "supplier": {
                                "id": supplier.id,
                                "name": supplier.name,
                                "address": supplier.address,
                                "contact": supplier.contact
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
        return jsonify({"message": "Error updating supplier. Please try again later"}), 500
