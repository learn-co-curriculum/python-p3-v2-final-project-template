from . import CURSOR, CONN


class User:
    
    def __init__(self, name, id = None):
        self.name = name

    def __repr__(self):
        return f"User ID:  || User Name: {self.name}"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # =>    PROPERTIES    <=  # # # # # # # # # # # # # #



    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError('Name must be a string')
        elif not (len(name) >= 1 and len(name) <= 20):
            raise ValueError('Name must be between 1 and 20 characters')
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
            sql = """ 
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                );

            """
            CURSOR.execute(sql)
            CONN.commit()
        
        except Exception as e:
            print('An Error Occured:', e)
            raise Exception
        
    @classmethod
    def drop_table(cls):
        try:
            sql = """ 
                DROP TABLE IF EXISTS users;
            """
            CURSOR.execute(sql)
            CONN.commit()
        except Exception as e:
            print('An Error Occured:', e)
            raise Exception
        
