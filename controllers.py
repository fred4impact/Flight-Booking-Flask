from flask import render_template, redirect, url_for, flash
from models import db, Flight, Booking
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
                destination=form.destination.data,
                departure=form.departure.data,
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
            booking = Booking(
                passenger_name=form.passenger_name.data,
                flight_id=form.flight_id.data
            )
            db.session.add(booking)
            db.session.commit()
            flash('Flight booked successfully!', 'success')
            return redirect(url_for('list_flights'))
        return render_template('book_flight.html', form=form)
