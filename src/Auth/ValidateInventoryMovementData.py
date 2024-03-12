from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired, NumberRange

class InventoryMovementsForm(FlaskForm):
    product_id = IntegerField('Product ID', validators=[
        DataRequired(message="Product ID is required"),
        NumberRange(min=1, message="Product ID must be a positive integer")
    ])
    quantity = IntegerField('Quantity', validators=[
        DataRequired(message="Quantity is required"),
        NumberRange(min=0, message="Quantiry must be a positive integer")
    ])
    type_id = IntegerField('Type ID', validators=[
        DataRequired(message="Type ID is required"),
        NumberRange(min=1, message="Type ID must be a positive integer")
    ])
