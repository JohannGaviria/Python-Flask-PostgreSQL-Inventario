from flask import Blueprint, jsonify, request
from src.Auth.ValidateInventoryMovementData import InventoryMovementsForm
from src.Models.InventoryMovementsModel import InventoryMovement
from src.Utils.Database import db
from src.Utils.Logger import Logger
from datetime import datetime
import traceback


main = Blueprint('createInventoryMovement', __name__)


# Ruta encargada de creación del movimiento de inventario
@main.post('api/inventoryMovement')
def create_inventory_movement():
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

            with db.session() as session:
                # Guardar el nuevo movimiento de inventorio
                new_inventory_movement = InventoryMovement(product_id, quantity, date, type_id)
                session.add(new_inventory_movement)
                session.commit()
            
            return jsonify({"message": "Inventory movement created successfully"}), 200

        # Si los datos no son validos
        else:
            # Obtener los errores de validación
            errors = form.errors
            return jsonify({"message": "Validation error", "errors": errors}), 400

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error creating inventory movement. Please try again later"}), 500