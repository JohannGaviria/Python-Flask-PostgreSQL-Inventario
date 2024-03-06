from flask import Blueprint, jsonify, request
from src.Models.SuppliersModel import Supplier
from src.Utils.Database import db


main = Blueprint('newSupplier', __name__)


# Ruta encargada de la creación de nuevos proveedores
@main.post('api/supplier')
def supplier():
    # Obtener los datos en formato JSON
    data = request.get_json()

    # Guardar cada uno de los datos en variables
    name = data['name']
    address = data['address']
    contact = data['contact']

    with db.session() as session:
        # Guardar el nuevo provedor en la base de datos
        new_supplier = Supplier(name, address, contact)
        session.add(new_supplier)
        session.commit()

    # Retornar mensaje de sastifación
    return jsonify({"message": "Supplier created successfully"}), 200