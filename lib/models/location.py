import sqlite3 

CONN = sqlite3.connect('lib/gym.db')
CURSOR = CONN.cursor()


class Location:
    def __init__(self, city, id = None):
        self.city = city
        self.id = id

    def display_info(self):
        print(f"Location: {self.name}")

    @classmethod
    def create_location_table(cls):
        query = """
            CREATE TABLE IS NOT EXISTS `location_table` (
            id INTEGER PRIMARY KEY,
            city TEXT);
        """
        CURSOR.execute(query)
        CONN.commit()

    # @classmethod 
    # def drop_table(cls):
    #     query = """
    #         DROP TABLE IF EXISTS `location_table`;
    #     """
    #     CURSOR.execute(query)
    #     CONN.commit()


    def save(self):
        query = """
            INSERT INTO `location_table` ( `city`)
            VALUES (?)
        """
        CURSOR.execute(query, (self.city))
        CONN.commit()
        self.id = CURSOR.lastrowid 

    @classmethod 
    def create_location_row(cls, city):
        city = cls(city)
        city.save()
        return city 
    
    @classmethod 
    def new_location_db(cls, row):
        location = cls (
                id = row[0],
                city = row[1]
            )
        print(location.city)
        return location 
    
    @classmethod 
    def get_all_locations(cls):
        sql = """
            SELECT * FROM location_table
        """
        return [cls.new_location_db(one_row) for one_row in CURSOR.execute(sql).fetchall()]
    
    @classmethod 
    def find_by_name(cls, city):
        sql = """
            SELECT * FROM location_table
            WHERE city = ? 
            LIMIT 1
        """
        row = CURSOR.execute(sql, (city)).fetchone()
        if not row:
            return None
        return Location(
            city = row[1],
            id = row[0]
        )


# Example locations
chicago_location = Location("Chicago")
st_louis_location = Location("St. Louis")
memphis_location = Location("Memphis")
