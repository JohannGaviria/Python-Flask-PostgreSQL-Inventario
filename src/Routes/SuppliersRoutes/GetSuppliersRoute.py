from flask import Blueprint, jsonify
from src.Models.SuppliersModel import Supplier
from src.Utils.Database import db
from src.Utils.Logger import Logger
import traceback


main = Blueprint('getSuppliers', __name__)


# Ruta encargada de obtener todos los proveedores
@main.get('api/suppliers')
def get_suppliers():
    try:
        # Consultar todos los proveedores en la base de datos
        suppliers = Supplier.query.all()
        # Crear una lista de diccionarios con la información de los proveedores
        suppliers_list = [{'id': supplier.id, 'name': supplier.name, 'address': supplier.address, 'contact': supplier.contact} for supplier in suppliers]
        
        # Devolver la lista de proveedores en formato JSON junto con el código de estado 200 (Éxito)
        return jsonify({'suppliers': suppliers_list}), 200       

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error getting suppliers. Please try again later"}), 500
