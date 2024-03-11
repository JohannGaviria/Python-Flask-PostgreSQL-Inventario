from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange


class ProductForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(message="Name is required"),
        Length(max=100, message="Name must be at most 100 characters long"),
    ])
    description = StringField('Description', validators=[
        DataRequired(message="Description is required"),
        Length(max=255, message="Description must be at most 255 characters long"),
    ])
    price = FloatField('Price', validators=[
        DataRequired(message="Price is required"),
        NumberRange(min=0, message="Price must be a non-negative number"),
    ])
    quantity = IntegerField('Quantity', validators=[
        DataRequired(message="Quantity is required"),
        NumberRange(min=0, message="Quantity must be a non-negative integer"),
    ])
    supplier_id = IntegerField('Supplier ID', validators=[
        DataRequired(message="Supplier ID is required"),
        NumberRange(min=1, message="Supplier ID must be a positive integer"),
    ])
    category_id = IntegerField('Category ID', validators=[
        DataRequired(message="Category ID is required"),
        NumberRange(min=1, message="Category ID must be a positive integer"),
    ])