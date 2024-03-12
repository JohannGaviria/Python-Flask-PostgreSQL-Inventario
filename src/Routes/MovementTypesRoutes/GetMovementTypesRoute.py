from flask import Blueprint, jsonify
from src.Models.MovementTypesModel import MovementType
from src.Utils.Logger import Logger
import traceback


main = Blueprint('getMovementTypes', __name__)


# Ruta encarga de obtener los tipos de movimientos
@main.get('api/movementTypes')
def get_movement_types():
    try:
        # Consultar todos los tipos de movimientos en la base de datos
        movement_types = MovementType.query.all()

        # Si existe algun registro de tipo de movimiento
        if movement_types:
            # Crear una lista de diccionarios con la información de los tipos de movimientos
            movement_types_list = [{'id': movement_type.id, 'name': movement_type.name} for movement_type in movement_types]

            # Devolver la lista de los tipos de movimientos en formato JSON
            return jsonify({"movement types": movement_types_list}), 200

        # Si no hay registro de tipo de movimiento devolver un mensaje
        return jsonify({"message": "Movement types not founds"}), 404

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error getting movement type. Please try again later"}), 500