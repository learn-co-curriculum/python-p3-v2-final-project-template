# lib/helpers.py
from models.itinerary import Trip
from models.itinerary import Activity


def exit_program():
    print("\033[32mGoodbye! \033[0m")
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
    print(trip) if trip else print(
        f'\033[31mTrip {name} not found. Please verify the name matches a valid trip. \033[0m')


def find_trip_by_id():
    id_ = input("\033[34mEnter the trip id:  \033[0m")
    trip = Trip.find_by_id(id_)
    print(trip) if trip else print(
        f'\033[31mTrip id {id_} not found. Please verify the id is a number that matches a valid trip \033[0m')


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
    while True:
        activity = input("\033[34mEnter activity:  \033[0m")
        description = input("\033[34mEnter description:  \033[0m")
        day = input("\033[34mEnter day:  \033[0m")
        trip_id = int(input("\033[34mEnter trip id: \033[0m"))

        try:
            price = float(input("\033[34mEnter price:  \033[0m"))
            break
        except ValueError:
            print("\033[31mInvalid price. Please enter a valid price. \033[0m")

    try:
        activity = Activity.create(activity, description, price, day, trip_id)
        return activity
    except ValueError as e:
        print(str(e))
        return None


def list_activities():
    activities = Activity.get_all()
    for activity in activities:
        print(activity)


def find_activity_by_name():
    activity_name = input("\033[34mEnter activity name:  \033[0m")
    activity = Activity.get_by_name(activity_name)
    print(activity) if activity else print(
        f"\033[31mActivity {activity_name} not found. Please verify the entry matches a valid activity. \033[0m")


def find_activity_by_id():
    id_ = input("\033[34mEnter activity id:  \033[0m")
    activity = Activity.find_by_id(id_)
    print(activity) if activity else print(
        f"\033[31mActivity id {id_} not found. Please verify id matches a valid activity. \033[0m")


def update_activity():
    id_ = input("\033[34m \033[0m"     "Enter activity id: ")
    if activity := Activity.find_by_id(id_):
        try:
            activity_name = input(
                "\033[34mEnter activity's new name:  \033[0m")
            activity.activity_name = activity_name
            description = input(
                "\033[34mEnter activity's new description:  \033[0m")
            activity.description = description
            price = float(
                input("\033[34mEnter new price of activity:  \033[0m"))
            activity.price = price
            day = input("\033[34mEnter new day:  \033[0m")
            activity.day = day
            trip_id = input("Enter new trip id: ")
            activity.trip_id = trip_id

            activity.update()
            print("\033[32mActivity updated successfully! \033[0m")

        except ValueError as exc:
            print(f"\033[31mError updating activity: {exc} \033[0m")
        except Exception as exc:
            print(f"\033[31mError updating activity: {exc} \033[0m")
    else:
        print(f"\033[31mActivity {id_} not found. \033[0m")


def delete_activity():
    id_ = input("\033[34mEnter activity id:  \033[0m")
    if activity := Activity.find_by_id(id_):
        activity.delete()
        print(f"\033[32mActivity id {id_} deleted. \033[0m")
    else:
        print(f"\033[31mActivity id {id_} not found. \033[0m")
