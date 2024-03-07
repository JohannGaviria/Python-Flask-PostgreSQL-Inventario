from flask import Blueprint, jsonify
from src.Models.SuppliersModel import Supplier
from src.Utils.Database import db
from src.Utils.Logger import Logger
import traceback


main = Blueprint('deleteSupplier', __name__)


# Ruta encargada de eliminar a los proveedores
@main.delete('api/supplier/<int:supplier_id>')
def delete_supplier(supplier_id):
    try:
        # Buscar el proveedor por su ID en la base de datos
        supplier = Supplier.query.get(supplier_id)
        
        # Si el proveedor no existe, devolver un mensaje de error
        if not supplier:
            return jsonify({"message": "Supplier not found"}), 404
        
        with db.session() as session:
            # Eliminar el proveedor de la base de datos
            session.delete(supplier)
            session.commit()
        
        # Devolver un mensaje de éxito
        return jsonify({"message": "Supplier deleted successfully"}), 200

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error deleting suppliers. Please try again later"}), 500