from flask import Blueprint, jsonify
from src.Models.InventoryMovementsModel import InventoryMovement
from src.Utils.Database import db
from src.Utils.Logger import Logger
import traceback


main = Blueprint('getInventoryMovement', __name__)


# Ruta encargada obtener un movimiento de inventario por su ID
@main.get('api/inventoryMovement/<int:inventory_movement_id>')
def get_inventory_movement(inventory_movement_id):
    try:
        return jsonify({"message": "ok"})

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error getting inventory movement. Please try again later"}), 500