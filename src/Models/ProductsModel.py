from src.Utils.Database import db


# Definición de la clase Product, que representa la tabla de productos en la base de datos.
class Product(db.Model):
    __tablename__ = 'products'

    # Columnas de la tabla products
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('product_categories.id'))

    # Constructor de la clase Product.
    def __init__(self, name, description, price, quantity, supplier_id, category_id):
        # Asigna los parámetros a los atributos de la instancia.
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.supplier_id = supplier_id
        self.category_id = category_id