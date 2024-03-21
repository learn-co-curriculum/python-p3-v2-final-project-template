from __init__ import CONN, CURSOR
from Visit import Visit


class User:
    
    def __init__(self, name, id = None):
        self.name = name

    def __repr__(self):
        return f"User ID: {self.id} || User Name: {self.name}"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # =>    PROPERTIES    <=  # # # # # # # # # # # # # #



    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError('Name must be a string')
        elif not (len(name) >= 1 and len(name) <= 16):
            raise ValueError('Name must be between 1 and 16 characters')
        else:
            self._name = name



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # => INSTANCE METHODS <=  # # # # # # # # # # # # # #
    


    # = = = = = = = = = = = = = => CRUD Methods   <= = = = = = = = = = = = = #

    def save(self):
        pass
    
    def update(self):
        pass

    def delete(self):
        pass
    

    # = = = = = = = = = = = = = =>  Aggregate Methods   <= = = = = = = = = = = #

    def get_visits():
        pass


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
        
