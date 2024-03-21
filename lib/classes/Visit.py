
class Visit:
    
    all = []
    
    def __init__(self, rating, description, date, user, restaurant):
        
        self.rating = rating
        self.description = description
        self.date = date
        self.user = user
        self.restaurant = restaurant
        type(self).all.append(self)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # =>    PROPERTIES    <=  # # # # # # # # # # # # # #
        
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if not isinstance(rating, int):
            raise ValueError('Rating must be a number between 1 and 10')
        elif not (len(rating) >= 1 and len(rating) <= 10):
            raise ValueError('Rating must be a number between 1 and 10')
        else:
            self._rating = rating

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise ValueError('Description must have letters')
        elif not (len(description) >= 1 and len(description) <= 100):
            raise ValueError('Description must be under 100 characters')
        else:
            self._description = description

    @property
    def date(self, date):
        return self._date
    
    # HOW SHOULD WE FORMAT DATE???
    @date.setter  
    def date(self, date):
        if not isinstance(date, str):
            raise ValueError("HELLLO")
        

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # => INSTANCE METHODS <=  # # # # # # # # # # # # # #




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # =>  CLASS METHODS   <=  # # # # # # # # # # # # # # 
    


    # = = = = = = = = = = = = = => Table Methods   <= = = = = = = = = = = = = #
    
    @classmethod
    def create_table(cls):
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