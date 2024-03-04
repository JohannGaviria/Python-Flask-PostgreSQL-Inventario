from src.Utils.Database import db


# Definición de la clase MovementType, que representa la tabla de tipos movimiento en la base de datos.
class MovementType(db.Model):
    __tablename__ = 'movement_types'

    # Columnas de la tabla movement_types
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # Constructor de la clase MovementType.
    def __init__(self, name):
        self.name = name