# lib/helpers.py

from models.flight import Flight
from models.passenger import Passenger
from models.booking import Booking

def load_data():
    Flight.create_table()
    Flight.create_initial_data()
    Passenger.create_table()
    Passenger.create_initial_data()
    Booking.create_table()
    Booking.create_initial_data()

def all_flights():
    print("Get all flights.")
    Flight.all_flights()

def all_passengers():
    print("Get all passengers.")
    Passenger.all_passengers()

def all_bookings():
    print("Get all bookings.")
    Booking.all_bookings()

def create_flight(name, number, origin, destination, departure_time, arrival_time):
    return Flight.create(name, number, origin, destination, departure_time, arrival_time)

def create_passenger(first_name, last_name, age, passport):
    return Passenger.create(first_name, last_name, age, passport)

def create_booking(passenger_id, flight_id, seat):
    return Booking.create(passenger_id, flight_id, seat)

def delete_flight(id):
    result = Flight.delete(id)
    if (result == None):
        print("Flight ID invalid, please try again. Hint: you will see it when you get all flights")
    else:
        print("Flight deleted successfully.")

def delete_passenger(id):
    result = Passenger.delete(id)
    if (result == None):
        print("Passenger ID invalid, please try again. Hint: you will see it when you get all passengers")
    else:
        print("Passenger deleted successfully.")

def delete_booking(id):
    result = Booking.delete(id)
    if (result == None):
        print("Booking ID invalid, please try again. Hint: you will see it when you get all bookings")
    else:
        print("Booking deleted successfully.")

def find_flight(id):
    result = Flight.find_by_id(id)
    if (result == None):
        print("Flight ID invalid, please try again. Hint: you will see it when you get all flights")
        return None
    else:
        print("Found flight:")
        Flight.print_flight_info(result)
        return result
    
def find_passenger(id):
    result = Passenger.find_by_id(id)
    if (result == None):
        print("Passenger ID invalid, please try again. Hint: you will see it when you get all passengers")
    else:
        print("Found flight:")
        Passenger.print_passenger_info(result)
        return result

def find_booking(id):
    result = Booking.find_by_id(id)
    if (result == None):
        print("Booking ID invalid, please try again. Hint: you will see it when you get all bookings")
    else:
        print("Found booking:")
        Booking.print_booking_info(result)
        return result

def all_passengers_per_flight(flight):
    result = flight.passengers()
    if (result == []):
        print("Flight ID invalid, please try again. Hint: you will see it when you get all flights")
    else:
        print("Found passengers:")
        for passenger in result:
            Passenger.print_passenger_info(passenger)

def all_flights_per_passenger(passenger):
    result = passenger.flights()
    if (result == []):
        print("Passenger ID invalid, please try again. Hint: you will see it when you get all passengers")
    else:
        print("Found flights:")
        for flight in result:
            Flight.print_flight_info(flight)

def all_bookings_per_flight(flight):
    result = flight.bookings()
    if (result == []):
        print("Passenger ID invalid, please try again. Hint: you will see it when you get all passengers")
    else:
        print("Found bookings:")
        for booking in result:
            Booking.print_booking_info(booking)

def all_bookings_per_passenger(passenger):
    result = passenger.bookings()
    if (result == []):
        print("Passenger ID invalid, please try again. Hint: you will see it when you get all passengers")
    else:
        print("Found bookings:")
        for booking in result:
            Booking.print_booking_info(booking)

def all_booking_info(booking):
    flight = Flight.find_by_id(booking.flight_id)
    passenger = Passenger.find_by_id(booking.passenger_id)
    if flight == None or passenger == None:
        print("Passenger / flight invalid, please try again. Hint: Check the booking and make sure the ids are present in passenger / flight.")
    else:
        Flight.print_flight_info(flight)
        Passenger.print_passenger_info(passenger)

def exit_program():
    print("Goodbye!")
    exit()
    