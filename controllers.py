from flask import render_template, redirect, url_for, flash
from models import db, Flight, Reservation
from forms import FlightForm, BookingForm

class FlightController:
    @staticmethod
    def list_flights():
        flights = Flight.query.all()
        return render_template('flights.html', flights=flights)

    @staticmethod
    def add_flight(form):
        if form.validate_on_submit():
            flight = Flight(
                flight_number=form.flight_number.data,
                departure=form.departure.data,
                destination=form.destination.data,
                departure_time=form.departure_time.data,
                price=form.price.data
            )
            db.session.add(flight)
            db.session.commit()
            flash('Flight added successfully!', 'success')
            return redirect(url_for('list_flights'))
        return render_template('add_flight.html', form=form)

class BookingController:
    @staticmethod
    def book_flight(form):
        if form.validate_on_submit():
            reservation = Reservation(
                flight_id=form.flight_id.data,
                passenger_name=form.passenger_name.data,
                passenger_email=form.passenger_email.data
            )
            db.session.add(reservation)
            db.session.commit()
            flash('Flight booked successfully!', 'success')
            return redirect(url_for('list_flights'))
        return render_template('book_flight.html', form=form)
