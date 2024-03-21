
class Restaurant:

    all = []
    
    def __init__(self, name, location, price, cuisine, phone, award, description, website_url, facilities, id = None):

        self.name = name
        self.location = location
        self.price = price
        self.cuisine = cuisine
        self.phone = phone
        self.award = award
        self.description = description
        self.website_url = website_url
        self.facilities = facilities
        type(self).all.append(self)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # =>    PROPERTIES    <=  # # # # # # # # # # # # # #
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError('Restaurant Name must be a word')
        else:
            self._name = name


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # => INSTANCE METHODS <=  # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # =>  CLASS METHODS   <=  # # # # # # # # # # # # # # 