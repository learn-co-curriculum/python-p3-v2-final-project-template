from models.__init__ import CONN, CURSOR

class Arcade:

    all = []

    def __init__(self, member, id=None):
        #this will pull the name from member
        self.member = member
        #based on membership level the person has access to 1, 2, or 3 locations
        # self.location = location 
        #this will pull the membership 
        self.id = id
        Arcade.add_access(self)

    @classmethod
    def add_new_location(cls, new_instance):
        cls.all.append(new_instance)

    @property
    def name(self, new_member):
        return new_member
    
    @name.setter
    def name(self, new_member):
        if not hasattr(self, "_member"):
            if type(new_member) == str:
                if 1<= len(new_member) <= 10:
                    raise ValueError("All new members must be betweeen 1 and 10 characters")
            raise TypeError("Name must be a string")
      
        self.name = new_member
    

    
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
            member_id INTEGER,
            location TEXT
            );
            """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO arcades ( arcade )
            VALUES (?)
            """
        CURSOR.execute(sql, (self.name, ))
        CONN.commit()

        self.id = CURSOR.lastrowid

Arcade.create_table()
    # database foreign keys/ references 

