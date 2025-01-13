from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, DateTimeField, EmailField
from wtforms.validators import DataRequired, Email, Length



class FlightForm(FlaskForm):
    flight_number = StringField('Flight Number', validators=[DataRequired()])
    departure = StringField('Departure', validators=[DataRequired()])
    destination = StringField('Destination', validators=[DataRequired()])
    departure_time = DateTimeField('Departure Time (YYYY-MM-DD HH:MM)', format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    submit = SubmitField('Add Flight')


class BookingForm(FlaskForm):
    passenger_name = StringField(
        'Passenger Name',
        validators=[DataRequired(), Length(max=100, message="Max 100 characters allowed")]
    )
    passenger_email = EmailField(
        'Passenger Email',
        validators=[DataRequired(), Email(message="Enter a valid email address"), Length(max=100)]
    )
    flight_id = IntegerField('Flight ID', validators=[DataRequired()])
    submit = SubmitField('Book Flight')
