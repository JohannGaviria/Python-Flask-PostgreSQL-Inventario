from flask import Blueprint, jsonify, request
from src.Auth.ValidateSupplierData import SupplierForm
from src.Models.SuppliersModel import Supplier
from src.Utils.Database import db
from src.Utils.Logger import Logger
import traceback


main = Blueprint('createSupplier', __name__)


# Ruta encargada de la creación de nuevos proveedores
@main.post('api/supplier')
def supplier():
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

            with db.session() as session:
                # Guardar el nuevo proveedor
                new_supplier = Supplier(name, address, contact)
                session.add(new_supplier)
                session.commit()

            return jsonify({"message": "Supplier created successfully"}), 200
        
        # Si los datos no son validos
        else:
            # Obtener los errors de validación
            errors = form.errors
            return jsonify({"message": "Validation error", "errors": errors}), 400

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error creating supplier. Please try again later"}), 500