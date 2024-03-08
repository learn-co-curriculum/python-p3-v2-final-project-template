from models.__init__ import CONN, CURSOR
from models.arcade import Arcade
from models.locale import Locale

class Member:
    all = []

    def __init__(self, name, tag, arcade_id, locale_id=None, id=None):
        self.name = name
        self.tag = tag
        self.arcade_id = arcade_id
        self.locale_id = locale_id
        self.id = id
        Member.add_new_member(self)

    @classmethod
    def add_new_member(cls, new_instance):
        cls.all.append(new_instance)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self, "_name"):
            self._name = new_name

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, new_tag):
        if not hasattr(self, "_tag"):
            self._tag = new_tag
    @property
    def locale_id(self):
        return self._locale_id
    
    @locale_id.setter
    def locale_id(self, new_locale_id):
        if isinstance(new_locale_id, str):
            if 3 <= len(new_locale_id) <= 25:
                    self._locale_id = new_locale_id
            else:
                raise ValueError("This location must be at least 7 and 25 characters long")
        else:
            raise TypeError("location name must be a string")

    def arcade(self):
        return [arcade for arcade in Arcade.all if arcade.member == self]

    def locale_id(self):
        return list({arcade.location for arcade in self.arcade()})
    
    def __repr__(self):
        return f'<Member id= "{self.id}" name= "{self.name}" tag= "{self.tag}" arcade_id= "{self.arcade_id}" locale_id= "{self.locale_id}" >'
    
    
    @classmethod
    def create_table(cls): 
        sql = """ 
            CREATE TABLE IF NOT EXISTS members(
            id INTEGER PRIMARY KEY,
            name TEXT,
            tag TEXT,
            arcade_id INTEGER,
            locale_id INTEGER
            );
            """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql="DROP TABLE IF EXISTS members;"
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        sql = """
            INSERT INTO members ( name, tag, arcade_id, locale_id)
            VALUES (?,?,?,?)
            """
        CURSOR.execute(sql, (self.name, self.tag, self.arcade_id, self.locale_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        
    @classmethod
    def find_by_id(cls , id):
        sql = """
              SELECT * FROM members
              WHERE id = ?
        """
        CURSOR.execute(sql, (id,))
        

    @classmethod
    def get_all(cls):
        sql = " SELECT * FROM members; "
        print(CURSOR.execute(sql).fetchall())

    @classmethod
    def delete_member(cls, member_name):
        member = cls.find_by_name(member_name)
        if member:
            cls.all.remove(member)
            sql = "DELETE FROM members WHERE name = ?"
            CURSOR.execute(sql, (member.name,))
            CONN.commit()
            print(f"Member {member_name} deleted")
        else: 
            print(f"Member {member_name} not found")

    @classmethod
    def find_by_name(cls, member_name):
        sql = "SELECT * FROM members WHERE name = ?"
        CURSOR.execute(sql, (member_name,))
        member_data = CURSOR.fetchone()
        if member_data:
            member = Member(*member_data)
            return member
        return None
    
    @classmethod
    def create_member(cls):
        name_input = input("Enter name: ")
        tag_input = input("Enter tag: ")
        location_input = input("Enter location: ")

        member = cls(name_input, tag_input, None, None)
        member.name = name_input
        member.tag = tag_input
        member.locale_id = location_input
        member.save()


    # @classmethod
    # def add_to_table(cls):
    #     sql = "INSERT INTO members "
             

    
   