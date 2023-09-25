# lib/helpers.py
from models.itinerary import Trip
from models.itinerary import Activity

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()


def create_trip():
    day = input("Enter which day the trip is: ")
    trip = input("Enter where the trip is: ")
    try:
        trip = Trip.create(day, trip)
        print("Added trip")
    except Exception as exc:
        print("Error creating department: ", exc)