from. import CURSOR, CONN

class Visit:
    
    all = []
    
    def __init__(self, rating, description, date, user_id, restaurant_id, id = None):
        
        self._id = id
        self.rating = rating
        self.description = description
        self.date = date
        self.user_id = user_id
        self.restaurant_id = restaurant_id
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
                INSERT INTO visits (rating, description, date, user_id, restaurant_id, id)
                VALUES (?, ?, ?, ?, ?, ?)
            ''')
            try:
                CURSOR.execute(sql, (self.rating, self.description, self.date, self.user_id, self.restaurant_id, self._id))
                CONN.commit()
                self._id = CURSOR.lastrowid  
                
            except Exception as e:
                print(e)
                raise Exception
    
    def update(self):
        sql = """
            UPDATE visits
            SET rating = ?, description = ?, date = ?, user_id = ?, restaurant_id = ?
            WHERE id = ?
        """
        try:
            CURSOR.execute(sql, (self.rating, self.description, self.date, self.user_id, self.restaurant_id, self._id))
            CONN.commit()
        except Exception as e:
            print('An Error Occurred:', e)
            raise Exception
    
    def delete(self):
        sql = """ 
            DELETE FROM visits
            WHERE id = ?
        """
        try:
            CURSOR.execute(sql, (self._id,))
            CONN.commit()
            # ipdb.set_trace()
        except Exception as e:
            print('An Error Occurred:', e)
            CONN.rollback()
            raise Exception

    # = = = = = = = = = = = = = =>  Aggregate Methods   <= = = = = = = = = = = #
        
    @classmethod
    def get_visits_by_restaurant_id(cls, restaurant_id):
        try:
            CURSOR.execute('SELECT * FROM visits WHERE restaurant_id = ?', (restaurant_id,))
            rows = CURSOR.fetchall()
            return [cls.instance_from_db(row) for row in rows]
        except Exception as e:
            CONN.rollback()
            print('An Error Occurred: ', e)
            raise Exception

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # =>  CLASS METHODS   <=  # # # # # # # # # # # # # # 
    
    # = = = = = = = = = = = = = => CRUD Methods   <= = = = = = = = = = = = = #

    @classmethod
    def create(cls, rating, description, date, user_id, restaurant_id, id = None):
        new_visit = cls(rating, description, date, user_id, restaurant_id, id)
        new_visit.save()
        return new_visit
    
    @classmethod
    def instance_from_db(cls, row):

        return cls(
            rating=row[1],
            description=row[2],
            date=row[3],
            user_id=row[4],
            restaurant_id=row[5],
            id=row[0]
        )
    
    @classmethod
    def get_all(cls):
        try:
            CURSOR.execute('SELECT * FROM visits')
            rows = CURSOR.fetchall()
            return [cls.instance_from_db(row) for row in rows]
        except Exception as e:
            CONN.rollback()
            print('An Error Occurred: ', e)
            raise Exception
    # = = = = = = = = = = = = = => Table Methods   <= = = = = = = = = = = = = #
    
    @classmethod
    def create_table(cls):
        sql = ('''
            CREATE TABLE IF NOT EXISTS visits (
            id INTEGER PRIMARY KEY,
            rating INTEGER,
            description TEXT,
            date TEXT,
            user_id INTEGER,
            restaurant_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (restaurant_id) REFERENCES restaurants(id) )
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
        
    