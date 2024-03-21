from. import CURSOR, CONN
class Visit:
    
    all = []
    
    def __init__(self, rating, description, date, user, restaurant, id = None):
        
        self.id = id
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
    def date(self):
        return self._date
    
    # HOW SHOULD WE FORMAT DATE???
    @date.setter  
    def date(self, date):
        # if not isinstance(date, str):
        #     raise ValueError("HELLLO")
        # else:
            self._date = date
        

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # => INSTANCE METHODS <=  # # # # # # # # # # # # # #
    def save(self):
            sql = ('''
                INSERT INTO visits (rating, description, date, user, restaurant, id)
                VALUES (?, ?, ?, ?, ?, ?)
            ''')
            try:
                CURSOR.execute(sql, (self.rating, self.description, self.date, self.user, self.restaurant, self.id))
                CONN.commit()
                self._id = CURSOR.lastrowid  
                
            except Exception as e:
                print(e)
                raise Exception



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # =>  CLASS METHODS   <=  # # # # # # # # # # # # # # 
    


    # = = = = = = = = = = = = = => Table Methods   <= = = = = = = = = = = = = #
    
    @classmethod
    def create_table(cls):
        sql = ('''
            CREATE TABLE IF NOT EXISTS visits (
            id INTEGER PRIMARY KEY,
            rating INTEGER,
            description TEXT,
            date TEXT,
            user INTEGER,
            restaurant INTEGER)
        ''')
        try:
            CURSOR.execute(sql)
            CONN.commit()
        except:
            raise ValueError('Failed to create table')
        
    @classmethod
    def drop_table(cls):
        """ Drop Visit Table"""
        sql = """
            DROP TABLE IF EXISTS visits;
            """ 
        try:
            CURSOR.execute(sql)
            CONN.commit()
        except:
            raise ValueError('Failed to drop table')
        
    @classmethod
    def create(cls, rating, description, date, user, restaurant, id = None):
        new_visit = cls(rating, description, date, user, restaurant, id)
        new_visit.save()
        return new_visit