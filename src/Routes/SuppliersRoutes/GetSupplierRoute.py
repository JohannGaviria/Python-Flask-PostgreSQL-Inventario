from flask import Blueprint, jsonify
from src.Models.SuppliersModel import Supplier
from src.Utils.Database import db
from src.Utils.Logger import Logger
import traceback


main = Blueprint('getSupplier', __name__)


# Ruta encargada de obtener un proveedor por su id
@main.get('api/supplier/<int:supplier_id>')
def get_supplier(supplier_id):
    try:
        # Buscar el proveedor por su ID en la base de datos
        supplier = Supplier.query.get(supplier_id)
        
        # Si el proveedor no existe, devolver un mensaje de error
        if not supplier:
            return jsonify({"message": "Supplier not found"}), 404
        
        # Devolver los datos del proveedor en formato JSON
        return jsonify({
            "id": supplier.id,
            "name": supplier.name,
            "address": supplier.address,
            "contact": supplier.contact
        }), 200
    
    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc)
        return jsonify({"message": "Error getting supplier. Please try again later"}), 500