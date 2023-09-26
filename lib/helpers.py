# lib/helpers.py
from models.itinerary import Trip
from models.itinerary import Activity


def exit_program():
    print( "\033[32mGoodbye! \033[0m")
    exit()


def create_trip():
    name = input("\033[34mEnter name for the trip: \033[0m")
    location = input("\033[34mEnter trip location: \033[0m")
    try:  
        location = Trip.create(name, location)
        print("\033[32mAdded trip! \033[0m")
    except Exception as exc:
        print("\033[31mError creating trip:  \033[0m", exc)

def list_trips():
    trips = Trip.get_all()
    for trip in trips:
        print(trip)

def find_trip_by_name():
    name = input("\033[34mEnter the trip name: \033[0m")
    trip = Trip.find_by_name(name)
    print(trip) if trip else print(f'\033[31mTrip {name} not found. Please verify the name matches a valid trip. \033[0m')

def find_trip_by_id():
    id_ = input("\033[34mEnter the trip id:  \033[0m")
    trip = Trip.find_by_id(id_)
    print(trip) if trip else print(f'\033[31mTrip id {id_} not found. Please verify the id is a number that matches a valid trip \033[0m')

def update_trip():
    id_ = input("\033[34mEnter the trip id:  \033[0m")
    if trip := Trip.find_by_id(id_):
        try:
            name = input("\033[34mEnter trip's new name:  \033[0m")
            trip.name = name
            location = input("\033[34mEnter trip's new location:  \033[0m")
            trip.location = location

            trip.update()
            print("\033[32mTrip changed successfully! \033[0m")
        except Exception as exc:
            print("\033[31mError updating trip. \033[0m", exc)
    else:
        print(f'\033[31mTrip {id_} not found. \033[0m')

def delete_trip():
    id_ = input("\033[34mEnter trip id:  \033[0m")
    if trip := Trip.find_by_id(id_):
        trip.delete()
        print(f'\033[32mTrip id {id_} deleted. \033[0m')
    else:
        print(f'\033[31mTrip id {id_} not found. \033[0m')


def create_activity():
    activity = input("Enter activity: ")
    description = input("Enter description: ")
    day = input("Enter day: ")

    try:
        price = float(input("Enter price: "))
    except ValueError:
        print("Invalid price. Please enter a valid price.")
        return None

    try:
        activity = Activity(activity, description, price, day)
        return activity
    except ValueError as e:
        print(str(e))
        return None
