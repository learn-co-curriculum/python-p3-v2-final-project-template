
class City:

    all_cities = []

    def __init__(self, name, concerts=None):
        self._name = name
        self.concerts = concerts or []
       
    #the getter of city names
    @property
    def name(self):
        return self._name
    #to have the user input a city and includes logic to raise errors
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("City name must be a string")
        if not new_name.strip():
            raise ValueError("City name cannot be blank")
        if not 2 <= len(new_name) <= 25:
            raise ValueError("City name length must be between 2 and 25 characters")
        self._name = new_name.strip()
    #to show concerts that are in a selected city
    def display_concerts(self):
        if self.concerts:
            print(f"Concerts in {self.name}: ")
            for concert in self.concerts:
                print(f": {concert}")
        else:
            print(f"No concerts found in {self.name}")
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
# City.add_city("Philadelphia", ["Concert 1", "Concert 2"])
# City.add_city("Pittsburgh", ["Concert 3"])
# City.add_city("Buffalo")
# City.add_city("Orlando", ["Concert 4"])
# City.add_city("San Diego")

# Create an instance of City
#city = City("New York", ["Concert 5", "Concert 6"])



# Call the method to select city and display concerts
city.select_city_and_display_concerts()


#list of all concert but for the city
def concerts(self):
       from models.concert import Concert
       return [concert for concert in Concert.all if concert.city == self]

       concert_list = [concert for concert in Concert.all if concert.venue == self]

       return concerts_list if len(concerts_list)> 0 else None
    

#city band 
def bands(self):
    return list(set([concert.band for concert in self.concerts()]))

def concert(self, date):
    for concert in self.concerts():
        if concert.date == date:
            return concert
    return None 

