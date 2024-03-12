from flask import Blueprint, jsonify, request
from src.Auth.ValidateInventoryMovementData import InventoryMovementsForm
from src.Models.InventoryMovementsModel import InventoryMovement
from src.Utils.Database import db
from src.Utils.Logger import Logger
from datetime import datetime
import traceback


main = Blueprint('updateInventoryMovement', __name__)


# Ruta encargada de actualizar un movimiento de inventario
@main.put('api/inventoryMovement/<int:inventory_movement_id>')
def update_inventory_movement(inventory_movement_id):
    try:
        # Obtener los datos en formato JSON enviados en la solicitud
        data = request.get_json()

        # Validar los datos del movimiento de inventario
        form = InventoryMovementsForm(data=data)

        # Si los datos son validos
        if form.validate():
            # Extraer los datos
            product_id = form.product_id.data
            quantity = form.quantity.data
            date = datetime.now()
            type_id = form.type_id.data

            # Buscar el movimiento de inventario por su ID en la base de datos
            inventory_movement = InventoryMovement.query.get(inventory_movement_id)

            # Si el movimiento de inventario no existe, devolver un mensaje de error
            if not inventory_movement:
                return jsonify({"message": "Inventory Movement type not found"}), 404
            
            # Actualizar los datos del movimiento de inventario si se proporcionan en la solicitud
            if product_id:
                inventory_movement.product_id = product_id
            if quantity:
                inventory_movement.quantity = quantity
            if date:
                inventory_movement.date = date
            if type_id:
                inventory_movement.type_id = type_id
            
            with db.session() as session:
                # Guardar los cambios en la base de datos
                session.commit()
            
                # Devolver mensaje de exitos junto con los datos actualizados del movimiento de inventario
                return jsonify({"message": "Inventory Movement updated successfully",
                                "Inventory Movement": {
                                    "id": inventory_movement.id,
                                    "product_id": inventory_movement.product_id,
                                    "quantity": inventory_movement.quantity,
                                    "date": inventory_movement.date,
                                    "type_id": inventory_movement.type_id
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
        return jsonify({"message": "Error updating inventory movement. Please try again later"}), 500