from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email


class SupplierForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(message="Name is required"),
        Length(max=100, message="Name must be at most 100 characters long"),
    ])
    address = StringField('Address', validators=[
        DataRequired(message="Address is required"),
        Length(max=200, message="Address must be at most 200 characters long"),
    ])
    contact = StringField('Contact', validators=[
        DataRequired(message="Contact is required"),
        Length(max=50, message="Contact must be at most 50 characters long"),
        Email(message="Invalid email format"),
    ])
