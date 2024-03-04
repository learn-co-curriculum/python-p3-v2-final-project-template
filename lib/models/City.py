from utils import custom_property

def name_conds(name):
    if not isinstance(name, str):
        raise TypeError("City name must be a string")
    if not name.strip():
        raise ValueError("City name cannot be blank")
    if not 2 <= len(name) <= 25:
        raise ValueError("City name length must be between 2 and 25 characters")
    return True

class City:

    all_cities = []

    def __init__(self, name, concerts=None):
        self.name = name
        self.concerts = concerts or []

    name = custom_property("name", name_conds)

    
       
    #the getter of city names
    # @property
    # def name(self):
    #     return self._name
    # #to have the user input a city and includes logic to raise errors
    # @name.setter
    # def name(self, new_name):
        # if not isinstance(new_name, str):
        #     raise TypeError("City name must be a string")
        # if not new_name.strip():
        #     raise ValueError("City name cannot be blank")
        # if not 2 <= len(new_name) <= 25:
        #     raise ValueError("City name length must be between 2 and 25 characters")
        # self._name = new_name.strip()

    # @classmethod
    # def name_conds(cls, name):
    #     if not isinstance(new_name, str):
    #         raise TypeError("City name must be a string")
    #     if not new_name.strip():
    #         raise ValueError("City name cannot be blank")
    #     if not 2 <= len(new_name) <= 25:
    #         raise ValueError("City name length must be between 2 and 25 characters")
    #     return True

    # Util.custom_property(City, "name", name_conds)

    # [name_getter, name_setter, name_deleter] = Util.custom_property("name", name_conds)
    # name = property(name_getter, name_setter, name_deleter)

    

    #to show concerts that are in a selected city
    def display_concerts(self):
        if self.concerts:
            print(f"Concerts in {self.name}: ")
            for concert in self.concerts:
                print(f": {concert}")
        else:
            print(f"No concerts found in {self.name}")

    #to add bands that are playing in the city and also to see whcih bands are playing by genre in a city:
    def add_concert(self, concert):
        self.concerts.append(concert)

    def bands_playing(self, genre = None, city = None):
        bands = set()
        for concert in self.concerts:
            if (genre is None or concert.genre == genre) and (city is None or concert.city == city):
            bands.add(concert.band_name)
        return list(bands)

    #to see if the city is the band's hometown:
    def is_home_city_of_band(self, band):
        from band import Band                                       #I only used the import here, to hopefully not have a circular import error
        if isinstance(band, Band) and band.home_city == self.name:
            print (f"This is {band.name}'s home city!")
        else:
            return False

    #creates and added the instance of a city to all cities
    @classmethod
    def add_city(cls, city_name, concerts=None):
        city = cls(city_name, concerts)
        cls.all_cities.append(city)

    @classmethod
    def get_all_cities(cls):
        return cls.all_cities
   
    def select_city_and_display_concerts(self):
    #User selects a city
        city_name = input("Enter the city name: ")
    #find the city and display the concerts
        found_city = None
        for city in City.all_cities:
            if city._name.lower() == city_name.lower():
                found_city = city
                break    #if break wasn't used the loop would keep going so this is for performance
        if found_city:
            found_city.display_concerts()
        else:
            print("City not found.")


   

    

    


# Add cities with concerts to City.all_cities
City.add_city("Philadelphia", ["Concert 1", "Concert 2"])
City.add_city("Pittsburgh", ["Concert 3"])
City.add_city("Buffalo")
City.add_city("Orlando", ["Concert 4"])
City.add_city("San Diego")

# Create an instance of City
city = City("New York", ["Concert 5", "Concert 6"])



# Call the method to select city and display concerts
# city.select_city_and_display_concerts()
import ipdb
ipdb.set_trace()


    