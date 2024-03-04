from src.Utils.Database import db


# Definición de la clase InventoryMovement, que representa la tabla de movimiento de inventario en la base de datos.
class InventoryMovement(db.Model):
    __tablename__ = 'inventory_movements'

    # Columnas de la tabla inventory_movements
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    type_id = db.Column(db.Integer, db.ForeignKey('movement_types.id'))

    # Constructor de la clase InventoryMovement.
    def __init__(self, product_id, quantity, date, type_id):
        # Asigna los parámetros a los atributos de la instancia.
        self.product_id = product_id
        self.quantity = quantity
        self.date = date
        self.type_id = type_id