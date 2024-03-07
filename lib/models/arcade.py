from models.__init__ import CONN, CURSOR

class Arcade:

    all = []

    def __init__(self, name, id=None):
        #this will pull the name from name
        self.name = name
        #based on membership level the person has access to 1, 2, or 3 locations
        # self.location = location 
        #this will pull the membership 
        self.id = id
        Arcade.add_access(self)

    @classmethod
    def add_new_location(cls, new_instance):
        cls.all.append(new_instance)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self, "_name"):
            if type(new_name) == str:
                if 1<= len(new_name) <= 25:
                    self._name = new_name
                else: 
                    raise ValueError("All new names must be betweeen 1 and 25 characters")
            else:
                raise TypeError("Name must be a string")
    

    
    @classmethod
    def locations(cls):
        return [locale.location for locale in Locale.all]
    
    @classmethod
    def members(cls):
        return [member.members for member in Member.all]
    
    
    @classmethod
    def add_access(cls, new_access):
        cls.all.append(new_access)

    def __repr__(self):
        return f'< Arcade id="{self.id}" name="{self.name}">'

    @classmethod
    def create_table(cls): 
        sql = """ 
            CREATE TABLE IF NOT EXISTS arcades(
            id INTEGER PRIMARY KEY,
            name TEXT
            );
            """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO arcades ( name )
            VALUES (?);
            """
        CURSOR.execute(sql, (self.name, ))
        CONN.commit()

        self.id = CURSOR.lastrowid
    
    @classmethod
    def drop_table(cls):
        sql= "DROP TABLE IF EXISTS arcades;"
        CURSOR.execute(sql)
        CONN.commit()

# Arcade.create_table()
    # database foreign keys/ references 

