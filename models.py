from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(10), nullable=False, unique=True)
    departure = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    departure_time = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Flight {self.flight_number} ({self.departure} -> {self.destination})>"

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), nullable=False)
    passenger_name = db.Column(db.String(100), nullable=False)
    passenger_email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Reservation {self.id} for {self.passenger_name}>"

# Refactored seed function
def seed():
    # Clear the table
    Flight.query.delete()
    db.session.commit()

    # Seed new data
    flights = [
        Flight(flight_number="FL123", departure="New York", destination="London", departure_time="2025-01-10 08:00", price=500.00),
        Flight(flight_number="FL456", departure="Los Angeles", destination="Tokyo", departure_time="2025-01-15 12:00", price=800.00),
    ]

    db.session.bulk_save_objects(flights)
    db.session.commit()
