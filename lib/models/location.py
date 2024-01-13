

class Location:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Location: {self.name}")

# Example locations
chicago_location = Location("Chicago")
st_louis_location = Location("St. Louis")
memphis_location = Location("Memphis")
