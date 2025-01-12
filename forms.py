from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length

class FlightForm(FlaskForm):
    destination = StringField('Destination', validators=[DataRequired(), Length(min=2, max=100)])
    departure = StringField('Departure', validators=[DataRequired(), Length(min=2, max=100)])
    price = FloatField('Price', validators=[DataRequired()])
    submit = SubmitField('Add Flight')

class BookingForm(FlaskForm):
    passenger_name = StringField('Passenger Name', validators=[DataRequired(), Length(min=2, max=100)])
    flight_id = IntegerField('Flight ID', validators=[DataRequired()])
    submit = SubmitField('Book Flight')
