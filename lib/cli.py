# lib/cli.py

from helpers import (
    load_data,
    exit_program,
    all_flights,
    all_passengers,
    all_bookings,
    create_flight,
    create_passenger,
    create_booking,
    delete_flight,
    delete_passenger,
    delete_booking,
    find_flight,
    find_passenger,
    find_booking,
    all_flights_per_passenger,
    all_passengers_per_flight,
    all_bookings_per_flight,
    all_bookings_per_passenger,
    all_booking_info
)
from models.passenger import Passenger
from models.flight import Flight
from models.booking import Booking

def main():
    load_data()
    while True:
        main_menu()

def main_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Flights information")
    print("2. Passengers information")
    print("3. Bookings information")
    
    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        flight_options()
    elif choice == "2":
        passenger_options()
    elif choice == "3":
        booking_options()
    else:
        print("Invalid choice")

def flight_options():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Get all Flights")
    print("2. Create a Flight")
    print("3. Find a Flight")
    print("4. Back to main menu")

    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        all_flights()
    elif choice == "2":
        create_flight_cli_options()
    elif choice == "3":
        id = input("Flight id > ")
        find_flight_cli_options(id)
    elif choice == "4":
        print("Going back to main menu")
        main_menu()
    else: 
        print("Invalid choice. Please pick from the available options.")

def create_flight_cli_options():
    print("Please select an option:")
    name = input("Flight Name > ")
    number = input("Flight number > ")
    origin = input("Origin City > ")
    destination = input("Destination City > ")
    departure_time = input("Departure Time > ")
    arrival_time = input("Arrival Time > ")
    new_flight = create_flight(name, int(number), origin, destination, departure_time, arrival_time)
    Flight.print_flight_info(new_flight)

def find_flight_cli_options(id):
    flight = find_flight(id)
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Delete this Flight")
    print("2. Get all Passengers in this Flight ID")
    print("3. Get all Bookings in this Flight ID")
    print("4. Back to main menu")
    
    choice = input("> ")
    if choice == "0":
        exit_program()
    if choice == "1":
        delete_flight(id)
    elif choice == "2":
        all_passengers_per_flight(flight)
    elif choice == "3":
        all_bookings_per_flight(flight)
    elif choice == "4":
        print("Going back to main menu")
        main_menu()
    else:
        print("Invalid choice. Please pick from the available options.")

def passenger_options():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Get all Passengers")
    print("2. Create a Passenger")
    print("3. Find a Passenger")
    print("4. Back to main menu")

    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        all_passengers()
    elif choice == "2":
        create_passenger_cli_options()
    elif choice == "3":
        id = input("Passenger id > ")
        find_passenger_cli_options(id)
    elif choice == "4":
        print("Going back to main menu")
    else:
        print("Invalid choice. Please pick from the available options.")

def create_passenger_cli_options():
    print("Please select an option:")
    first_name = input("First name > ")
    last_name = input("Last name > ")
    age = input("Age > ")
    passport = input("Passport > ")
    new_passenger = create_passenger(first_name, last_name, int(age), passport)
    Passenger.print_passenger_info(new_passenger)

def find_passenger_cli_options(id):
    passenger = find_passenger(id) 
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Delete this Passenger")
    print("2. Get all Flights of this Passenger ID")
    print("3. Get all Bookings of this Passenger ID")
    print("4. Back to main menu")
    
    choice = input("> ")
    if choice == "0":
        exit_program()
    if choice == "1":
        delete_passenger(id)
    elif choice == "2":
        all_flights_per_passenger(passenger)
    elif choice == "3":
        all_bookings_per_passenger(passenger)
    elif choice == "4":
        print("Going back to main menu.")
        main_menu()
    else:
        print("Invalid choice. Please pick from the available options.")

def booking_options():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Get all Bookings")
    print("2. Create a Booking")
    print("3. Find a Booking")
    print("4. Back to main menu")

    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        all_bookings()
    elif choice == "2":
        print("Create a Booking")
        create_booking_cli_options()
    elif choice == "3":
        id = input("Booking id > ")
        find_booking_cli_options(id)
    elif choice == "4":
        print("Going back to main menu")
    else:
        print("Invalid choice. Please pick from the available options.")

def create_booking_cli_options():
    print("Please select an option:")
    passenger_id = input("Passenger ID: > ")
    flight_id = input("Flight ID > ")
    seat = input("Seat: > ")
    new_booking = create_booking(passenger_id, flight_id, seat)
    Booking.print_booking_info(new_booking)

def find_booking_cli_options(id):
    booking = find_booking(id) 
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Delete this Booking")
    print("2. Get the Flight and Passenger info of this Booking ID")
    print("3. Back to main menu")
    
    choice = input("> ")
    if choice == "0":
        exit_program()
    if choice == "1":
        delete_booking(id)
    elif choice == "2":
        all_booking_info(booking)
    elif choice == "3":
        print("Going back to main menu.")
        main_menu()
    else:
        print("Invalid choice. Please pick from the available options.")

if __name__ == "__main__":
    main()
