import sqlite3 

CONN = sqlite3.connect('lib/gym.db')
CURSOR = CONN.cursor()

class Member:
    def __init__(self, first_name, last_name, level, id = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.level = level

    @classmethod 
    def create_member_table(cls):
        query = """
            CREATE TABLE IF NOT EXISTS `member_table` (
            id INTEGER PRIMARY KEY, 
            first_name TEXT, 
            last_name TEXT, 
            level TEXT);
        """
        CURSOR.execute(query)
        CONN.commit()

    # @classmethod 
    # def drop_table(cls):
    #     query = """
    #         DROP TABLE IF EXISTS `member_table`;
    #     """
    #     CURSOR.execute(query)
    #     CONN.commit()

    def save(self):
        query = """
            INSERT INTO `member_table` ( `first_name`, `last_name`, `level`)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(query, (self.first_name, self.last_name, self.level))
        CONN.commit()
        self.id = CURSOR.lastrowid 

    @classmethod 
    def create_member_row(cls, first_name, last_name, level):
        member = cls(first_name, last_name, level)
        member.save()
        return member 
    
    @classmethod 
    def new_member_db(cls, row):
        member = cls (
                id = row[0],
                first_name = row[1],
                last_name = row[2],
                level = row[3]
            )
        print(member.first_name, member.last_name, member.level)
        return member
    
    @classmethod 
    def get_all_members(cls):
        sql = """
            SELECT * FROM members
        """
        return [cls.new_member_db(one_row) for one_row in CURSOR.execute(sql).fetchall()]
    
    @classmethod 
    def find_by_name(cls, first_name, last_name):
        sql = """
            SELECT * FROM members
            WHERE first_name = ? 
            AND last_name = ?
            LIMIT 1
        """
        row = CURSOR.execute(sql, (first_name, last_name)).fetchone()
        if not row:
            return None
        return Member(
            first_name = row[1],
            last_name = row[2],
            id = row[0]
        )

class Location:
    def __init__(self, city, id = None):
        self.city = city
        self.id = id

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
            SELECT * FROM location
        """
        return [cls.new_location_db(one_row) for one_row in CURSOR.execute(sql).fetchall()]
    
    @classmethod 
    def find_by_name(cls, city):
        sql = """
            SELECT * FROM location
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

    
