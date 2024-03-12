from flask import Blueprint, jsonify
from src.Models.InventoryMovementsModel import InventoryMovement
from src.Utils.Logger import Logger
import traceback


main = Blueprint('getInventoryMovements', __name__)


# Ruta encargada de obtener los movimientos del inventario
@main.get('api/inventoryMovements')
def get_inventory_movement():
    try:
        # Consultar todos los movimientos del inventario
        inventory_movements = InventoryMovement.query.all()

        # Si existe algun registro de movmiento de inventario
        if inventory_movements:
            # Crear una lista de diccionarios con la información de los movimientos del inventario
            inventory_movements_list = [{
                'id': inventory_movement.id,
                'product_id': inventory_movement.product_id,
                'quantity': inventory_movement.quantity,
                'date': inventory_movement.date,
                'type_id': inventory_movement.type_id
            } for inventory_movement in inventory_movements]

            # Devolver la lista de los movimientos de inventario en formato JSON
            return jsonify({"Inventory Movement": inventory_movements_list}), 200

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error getting inventory movements. Please try again later"}), 500