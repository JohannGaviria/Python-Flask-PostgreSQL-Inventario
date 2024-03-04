from src.Utils.Database import db


# Definición de la clase Supplier, que representa la tabla de provedores en la base de datos.
class Supplier(db.Model):
    __tablename__ = 'suppliers'

    # Columnas de la tabla suppliers
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    contact = db.Column(db.String)

    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact