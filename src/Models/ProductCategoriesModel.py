from src.Utils.Database import db


# Definición de la clase ProductCategory, que representa la tabla de catrgorias producto en la base de datos.
class ProductCategory(db.Model):
    __tablename__ = 'product_categories'

    # Columnas de la tabla product_categories
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name
