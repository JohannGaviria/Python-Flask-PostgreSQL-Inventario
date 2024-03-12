from flask import Blueprint, jsonify
from src.Models.InventoryMovementsModel import InventoryMovement
from src.Utils.Database import db
from src.Utils.Logger import Logger
import traceback


main = Blueprint('deleteInventoryMovement', __name__)


# Ruta encargada de eliminar un movimiento de inventario
@main.delete('api/inventoryMovement/<int:inventory_movement_id>')
def delete_inventory_movement(inventory_movement_id):
    try:
        # Buscar el movimiento de inventario por su ID en la base de datos
        inventory_movement = InventoryMovement.query.get(inventory_movement_id)
        
        # Si el movimiento de inventario no existe, devolver un mensaje de error
        if not inventory_movement:
            return jsonify({"message": "Inventory movement type not found"}), 404
        
        with db.session() as session:
            # Eliminar el movimiento de inventario de la base de datos
            session.delete(inventory_movement)
            session.commit()
        
        # Devolver un mensaje de éxito
        return jsonify({"message": "inventory movement type deleted successfully"}), 200

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error deleting inventory movement. Please try again later"}), 500