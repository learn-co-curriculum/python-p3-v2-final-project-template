
class Restaurant:

    
    def __init__(self, name, address, ward, cuisine, price, website_url, award, misc, description, id = None):

        self.name = name
        self.address = address
        self.ward = ward
        self.cuisine = cuisine
        self.price = price
        self.website_url = website_url
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
            raise ValueError('Restaurant Name must be a word')
        else:
            self._name = name

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        if not isinstance(address, str):
            raise ValueError('Restaurant Address must be a word')
        else:
            self._address = address

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
            price, INT,
            website_url TEXT,
            award TEXT,
            misc, TEXT,
            description TEXT
            )
            """

        try:
            CURSOR.execute()
            CONN.commit()
        except:
            raise ValueError('')
        
    @classmethod
    def drop_table(cls):
        try:
            CURSOR.execute()
            CONN.commit()
        except:
            raise ValueError('')