class Band:
    def __init__(self, name, members, gender, home_city):
        self.name = name  # This will call the @name.setter method
        self.members = members
        self.gender = gender
        self.home_city = home_city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Band name must be a non-empty string")

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, members):
        if isinstance(members, list) and len(members) > 0:
            self._members = members
        else:
            raise ValueError("Members must be a non-empty list")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if isinstance(gender, str) and gender in ['male', 'female', 'mixed', 'other']:
            self._gender = gender
        else:
            raise ValueError("Gender must be 'male', 'female', 'mixed', or 'other'")

    @property
    def home_city(self):
        return self._home_city

    @home_city.setter
    def home_city(self, home_city):
        if isinstance(home_city, str) and len(home_city) > 0:
            self._home_city = home_city
        else:
            raise ValueError("Home city must be a non-empty string")
