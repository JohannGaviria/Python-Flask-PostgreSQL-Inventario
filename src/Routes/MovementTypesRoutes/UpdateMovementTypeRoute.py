from flask import Blueprint, jsonify, request
from src.Auth.ValidateMovementTypeData import MovementTypeForm
from src.Models.MovementTypesModel import MovementType
from src.Utils.Database import db
from src.Utils.Logger import Logger
import traceback


main = Blueprint('uptadeMovementType', __name__)


# Ruta encargada de actualizar el tipo de movimiento
@main.put('api/movementType/<int:movement_type_id>')
def update_movement_type(movement_type_id):
    try:
        # Obtener los datos en formato JSON enviados en la solicitud
        data = request.get_json()

        # Validar los datos del producto
        form = MovementTypeForm(data=data)

        # Si los datos son validos
        if form.validate():
            # Extraer los datos
            name = form.name.data

            # Buscar el tipo de movimiento por su ID en la base de datos
            movement_type = MovementType.query.get(movement_type_id)

            # Si el tipo de movimiento no existe, devolver un mensaje de error
            if not movement_type:
                return jsonify({"message": "Movement type not found"}), 404
            
            # Actualizar los datos del tipo de movimiento si se proporcionan en la solicitud
            if name:
                movement_type.name = name
            
            with db.session() as session:
                # Guardar los cambios en la base de datos
                session.commit()
            
                # Devolver mensaje de exitos junto con los datos actualizados del tipo de movimiento
                return jsonify({"message": "Movement type updated successfully",
                                "movement type": {
                                    "id": movement_type.id,
                                    "name": movement_type.name
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
        return jsonify({"message": "Error updating movement type. Please try again later"}), 500