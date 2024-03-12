from flask import Blueprint, jsonify
from src.Models.MovementTypesModel import MovementType
from src.Utils.Logger import Logger
import traceback


main = Blueprint('getMovementType', __name__)


# Ruta encarga de obtener un tipo de movimiento por su ID
@main.get('api/movementType/<int:movement_type_id>')
def get_movement_type(movement_type_id):
    try:
        # Buscar el tipo de movimiento por su ID en la base de datos
        movement_type = MovementType.query.get(movement_type_id)

        # Si el tipo de movimiento no existe, devolver un mensaje de error
        if not movement_type:
            return jsonify({"message": "Movement type not found"}), 404
        
        # Devolver los datos del tipo de movimiento en formato JSON
        return jsonify({"id": movement_type.id, "name": movement_type.name}), 200

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error gettting movement type. Please try again later"}), 500