from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from config import Config
from models import db, Flight, Reservation, seed
from controllers import FlightController, BookingController
from forms import FlightForm, BookingForm
import secrets

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = secrets.token_hex(16)

# Initialize SQLAlchemy and Flask-Migrate
db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    # Create database tables and seed data if necessary
    db.create_all()
    seed()

@app.route('/')
def home():
    """Home page for the Flight Booking System."""
    return render_template('index.html')

@app.route('/flights', methods=['GET', 'POST'])
def list_flights():
    """Lists all available flights."""
    return FlightController.list_flights()

@app.route('/add_flight', methods=['GET', 'POST'])
def add_flight():
    """Adds a new flight."""
    form = FlightForm()
    if form.validate_on_submit():
        return FlightController.add_flight(form)
    return render_template('add_flight.html', form=form)

@app.route('/book_flight', methods=['GET', 'POST'])
def book_flight():
    """Books a flight for a passenger."""
    form = BookingForm()
    if form.validate_on_submit():
        return BookingController.book_flight(form)
    return render_template('book_flight.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
