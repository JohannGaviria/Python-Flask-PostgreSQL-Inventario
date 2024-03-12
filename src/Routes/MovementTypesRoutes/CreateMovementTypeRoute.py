from flask import Blueprint, jsonify, request
from src.Auth.ValidateMovementTypeData import MovementTypeForm
from src.Models.MovementTypesModel import MovementType
from src.Utils.Database import db
from src.Utils.Logger import Logger
import traceback


main = Blueprint('createMovementType', __name__)


# Ruta encargada de la creación de tipo de movimiento
@main.post('api/movementType')
def create_movement_type():
    try:
        # Obtener los datos en formato JSON enviados en la solicitud
        data = request.get_json()

        # Validar los datos del tipo de movimiento
        form = MovementTypeForm(data=data)

        # Si los datos son validos
        if form.validate():
            # Extraer los datos
            name = form.name.data

            with db.session() as session:
                # Guardar el nuevo tipo de movimiento
                new_movement_type = MovementType(name)
                session.add(new_movement_type)
                session.commit()
            return jsonify({"message": "Movement type created successfully"}), 200

        # Si los datos no son validos
        else:
            # Obtener los errores de validación
            errors = form.errors
            return jsonify({"message": "Validation error", "errors": errors}), 400

    except Exception as ex:
        # Registrar cualquier excepción ocurrida durante el proceso
        Logger.add_to_log('error', str(ex))
        Logger.add_to_log('error', traceback.format_exc())
        return jsonify({"message": "Error creating movement type. Please try again later"}), 500