from __init__ import CURSOR, CONN

class Restaurant:

    
    def __init__(self, name, address, ward, cuisine, price, website, award, misc, description, id = None):

        self.name = name
        self.address = address
        self.ward = ward
        self.cuisine = cuisine
        self.price = price
        self.website = website
        self.award = award
        self.misc = misc
        self.description = description



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # =>    PROPERTIES    <=  # # # # # # # # # # # # # #
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError('Restaurant Name must be a string')
        elif len(name) < 1 or len(name) > 75:
            raise ValueError('Restaurant Name must be between 1 and 75 characters')
        else:
            self._name = name

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        if not isinstance(address, str):
            raise ValueError('Restaurant Address must be a string')
        elif len(address) < 1 or len(address) > 150:
            raise ValueError('Restaurant Address must be between 1 and 150 characters')
        else:
            self._address = address

    @property
    def ward(self):
        return self._ward
    
    @ward.setter
    def ward(self, ward):
        if not isinstance(ward, str):
            raise ValueError('Ward must be a string')
        elif len(ward) < 1 or len(ward) > 50:
            raise ValueError('Ward must be between 1 and 50 characters')
        else:
            self._ward = ward

    @property
    def cuisine(self):
        return self._cuisine
    
    @cuisine.setter
    def cuisine(self, cuisine):
        if not isinstance(cuisine, str):
            raise ValueError('Cuisine must be a string')
        elif len(cuisine) < 1 or len(cuisine) > 50:
            raise ValueError('Cuisine must be between 1 and 20 characters')
        else:
            self._cuisine = cuisine

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if not isinstance(price, str):
            raise ValueError('Price must a string')
        elif len(price) < 1 or len(price) > 4:
            raise ValueError('Price must be between 1 and 4 characters')
        else:
            self._price = price
    
    @property
    def website(self):
        return self._website
    
    @website.setter
    def website(self, website):
        if not isinstance(website, str):
            raise ValueError('Website must be a string')
        elif len(website) < 1 or len(website) > 100:
            raise ValueError('Website must be between 1 and 100 characters')
        else:
            self._website = website

    @property
    def award(self):
        return self._award
    
    @award.setter
    def award(self, award):
        if not isinstance(award, str):
            raise ValueError('Award must be a string')
        elif len(award) < 1 or len(award) > 15:
            raise ValueError('Award must be between 1 and 15 characters')
        else:
            self._award = award

    @property
    def misc(self):
        return self._misc
    
    @misc.setter
    def misc(self, misc):
        if not isinstance(misc, str):
            raise ValueError('Misc must be a string')
        elif len(misc) < 1 or len(misc) > 100:
            raise ValueError('Misc must be between 1 and 100 characters')
        else:
            self._misc = misc
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # => INSTANCE METHODS <=  # # # # # # # # # # # # # #


            
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # =>  CLASS METHODS   <=  # # # # # # # # # # # # # # 
    


    # = = = = = = = = = = = = = => Table Methods   <= = = = = = = = = = = = = #
    
    @classmethod
    def create_table(cls):
        """ Create restaurant table """
        sql = """
            CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT,
            ward TEXT,
            cuisine TEXT,
            price, ,
            website TEXT,
            award TEXT,
            misc, TEXT,
            description TEXT
            )
            """

        try:
            CURSOR.execute(sql)
            CONN.commit()
        except:
            raise ValueError('')
        
    @classmethod
    def drop_table(cls):
        """ Drop Restaurant Table"""
        sql = """"
            DROP TABLE IF EXISTS restaurants;
            """
        try:
            CURSOR.execute(sql)
            CONN.commit()
        except:
            raise ValueError('')