from . import CURSOR, CONN
from classes.Visit import Visit
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
        self.id = id



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
        elif len(website) > 100:
            raise ValueError('Website must be between 0 and 100 characters')
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
        elif len(misc) > 200:
            raise ValueError('Misc must be between 0 and 100 characters')
        else:
            self._misc = misc
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # => INSTANCE METHODS <=  # # # # # # # # # # # # # #

    # = = = = = = = = = = = = = => CRUD Methods   <= = = = = = = = = = = = = #
    def save(self):
        sql = """ 
            INSERT INTO restaurants (name, address, ward, cuisine, price, website, award, misc, description, id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ? )
        """
        try:
            CURSOR.execute(sql, (self.name, self.address, self.ward, self.cuisine, self.price, self.website, self.award, self.misc, self.description, self.id))
            CONN.commit()
            self._id = CURSOR.lastrowid
        except Exception as e:
            CONN.rollback()
            print('An Error Occurred:', e)
            raise Exception
        
        return self
    





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # =>  CLASS METHODS   <=  # # # # # # # # # # # # # # 
    
    # = = = = = = = = = = = = = => CRUD Methods   <= = = = = = = = = = = = = #
    @classmethod
    def create(cls, name, address, ward, cuisine, price, website, award, misc, description, id = None):
        new_restaurant = cls(name, address, ward, cuisine, price, website, award, misc, description, id)
        new_restaurant.save()
        return new_restaurant
        
    @classmethod
    def instance_from_db(cls, row):

        return cls(
            row["Name"], #name
            row["Address"], #address
            row["Wards"], #ward
            row["Cuisine"], #cuisine
            row["Price"], #price
            row["WebsiteUrl"], #website
            row["Award"], #award
            row["FacilitiesAndServices"], #misc
            row["Description"], #description
            None
         )   

    @classmethod
    def get_all(cls, limit=None, offset=None):
        try:
            query = 'SELECT * FROM restaurants'
            if limit is not None and offset is not None:
                query += f' LIMIT {limit} OFFSET {offset}'
            CURSOR.execute(query)
            rows = CURSOR.fetchall()
            return [cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[0]) for row in rows]
        except Exception as e:
            CONN.rollback()
            print('An Error Occurred: ', e)
            raise Exception
        

    @classmethod
    def get_restaurants_by_location(cls, location, limit=None, offset=None):
        try:
            query = f'SELECT * FROM restaurants WHERE ward = ?'
            if limit is not None and offset is not None:
                query += f' LIMIT {limit} OFFSET {offset}'
            CURSOR.execute(query, (location,))
            rows = CURSOR.fetchall()
            return [cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[0]) for row in rows]
        except Exception as e:
            CONN.rollback()
            print('An Error Occurred: ', e)
            raise Exception
    
    @classmethod
    def get_restaurants_by_cuisine(cls, cuisine, limit=None, offset=None):
        try:
            query = "SELECT * FROM restaurants WHERE cuisine = ?"
            params = (cuisine,)
            if limit is not None and offset is not None:
                query += " LIMIT ? OFFSET ?"
                params += (limit, offset)
            CURSOR.execute(query, params)
            rows = CURSOR.fetchall()
            return [cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[0]) for row in rows]
        except Exception as e:
            CONN.rollback()
            print('An Error Occurred: ', e)
            raise Exception

    @classmethod
    def get_count_by_cuisine(cls, cuisine):
        try:
            CURSOR.execute("SELECT COUNT(*) FROM restaurants WHERE cuisine = ?", (cuisine,))
            count = CURSOR.fetchone()[0]
            return count
        except Exception as e:
            CONN.rollback()
            print('An Error Occurred: ', e)
            raise Exception
        
    @classmethod
    def get_total_count(cls):
        try:
            CURSOR.execute('SELECT COUNT(*) FROM restaurants')
            count = CURSOR.fetchone()[0]
            return count
        except Exception as e:
            CONN.rollback()
            print('An Error Occurred: ', e)
            raise Exception
        
    @classmethod
    def get_count_by_location(cls, location):
        try:
            CURSOR.execute('SELECT COUNT(*) FROM restaurants WHERE ward = ?', (location,))
            count = CURSOR.fetchone()[0]
            return count
        except Exception as e:
            CONN.rollback()
            print('An Error Occurred: ', e)
            raise Exception

    @classmethod
    def get_total_pages(cls, restaurants_per_page):
        total_restaurants = cls.get_total_count()
        total_pages = (total_restaurants + restaurants_per_page - 1) // restaurants_per_page
        return total_pages
    
    @classmethod
    def get_by_id(cls, restaurant_id):
        try:
            CURSOR.execute("SELECT * FROM restaurants WHERE id = ?", (restaurant_id,))
            row = CURSOR.fetchone()
            if row:
                return cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[0])
            else:
                return None
        except Exception as e:
            CONN.rollback()
            print('An Error Occurred: ', e)
            raise Exception
        
    #Association Methods
    def visits(self):
        sql = """ 
            SELECT *
            FROM visits
            WHERE restaurant_id = ?
        """
        try:
            CURSOR.execute(sql, (self.id,))
            CONN.commit()
            rows = CURSOR.fetchall()
            return [ Visit(row[1],row[2],row[3],row[4],row[5],row[0]) for row in rows]
        except Exception as e:
            print('An Error Occurred:', e)
            raise Exception






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
            price TEXT,
            website TEXT,
            award TEXT,
            misc TEXT,
            description TEXT
            );
            """

        try:
            CURSOR.execute(sql)
            CONN.commit()
        except:
            CONN.rollback()
            raise ValueError('')
        
    @classmethod
    def drop_table(cls):
        """ Drop Restaurant Table"""
        sql = """
            DROP TABLE IF EXISTS restaurants;
            """
        try:
            CURSOR.execute(sql)
            CONN.commit()
        except:
            CONN.rollback()
            raise ValueError('')
        


