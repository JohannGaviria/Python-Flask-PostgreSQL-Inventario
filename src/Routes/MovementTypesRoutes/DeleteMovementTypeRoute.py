from flask import Blueprint, jsonify, request
from src.Auth.ValidateMovementTypeData import MovementTypeForm
from src.Models.MovementTypesModel import MovementType
from src.Utils.Database import db
from src.Utils.Logger import Logger
import traceback


main = Blueprint('deleteMovementType', __name__)


# Ruta encargada de eliminar el tipo de movimiento
@main.delete('api/movementType/<int:movement_type_id>')
def delete_product_categorie(movement_type_id):
    try:
        # Buscar el tipo de movimiento por su ID en la base de datos
        movement_type = MovementType.query.get(movement_type_id)
        
        # Si el tipo de movimiento no existe, devolver un mensaje de error
        if not movement_type:
            return jsonify({"message": "Movement type not found"}), 404
        
        with db.session() as session:
            # Eliminar el tipo de movimiento de la base de datos
            session.delete(movement_type)
            session.commit()
        
        # Devolver un mensaje de éxito
        return jsonify({"message": "Movement type deleted successfully"}), 200

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error deleting movement type. Please try again later"}), 500