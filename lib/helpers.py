# lib/helpers.py
from models.itinerary import Trip
from models.itinerary import Activity


def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()


def create_trip():
    name = input("Enter name for the trip is: ")
    location = input("Enter where the trip is: ")
    try:
        location = Trip.create(name, location)
        print("Added trip!")
    except Exception as exc:
        print("Error creating trip: ", exc)


def list_trips():
    trips = Trip.get_all()
    for trip in trips:
        print(trip)


def find_trip_by_name():
    name = input("Enter the trip name: ")
    trip = Trip.find_by_name(name)
    print(trip) if trip else print(
        f'Trip {name} not found. Please verify the name matches a valid trip')


def find_trip_by_id():
    id_ = input("Enter the trip id: ")
    trip = Trip.find_by_id(id_)
    print(trip) if trip else print(
        f'Trip id {id_} not found. Please verify the id is a number that matches a valid trip')


def update_trip():
    id_ = input("Enter trip id: ")
    if trip := Trip.find_by_id(id_):
        try:
            name = input("Enter trip's new name: ")
            trip.name = name
            location = input("Enter trip's new location: ")
            trip.location = location

            trip.update()
            print("Trip changed successfully!")
        except Exception as exc:
            print("Error updating trip.", exc)
    else:
        print(f'Trip {id_} not found.')


def delete_trip():
    id_ = input("Enter trip id: ")
    if trip := Trip.find_by_id(id_):
        trip.delete()
        print(f'Trip id {id_} deleted.')
    else:
        print("Trip id {id_} not found.")


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


def list_activities():
    activities = Activity.get_all()
    for activity in activities:
        print(activity)


def find_activity_by_name():
    activity_name = input("Enter activity: ")
    activity = Activity.get_by_name(activity_name)
    print(activity) if activity else print(
        f'Activity {activity_name} not found. Please verify the entry matches a valid activity.')


def find_activity_by_id():
    id_ = input("Enter activity id: ")
    activity = Activity.find_by_id(id_)
    print(activity) if activity else print(
        f'Activity id {id_} not found. Please verify id matches a valid activity.')


def update_activity():
    id_ = input("Enter activity id: ")
    if activity := Activity.find_by_id(id_):
        try:
            activity_name = input("Enter activity's new name: ")
            activity.activity_name = activity_name
            description = input("Enter activity's new description: ")
            activity.description = description
            price = float(input("Enter new price of activity: "))
            activity.price = price
            day = input("Enter new day: ")
            activity.day = day

            activity.update()
            print("Activity updated successfully.")

        except ValueError as exc:
            print(f"Error updating activity: {exc}")
        except Exception as exc:
            print(f"Error updating activity: {exc}")

    else:
        print(f"Activity {id_} not found.")
