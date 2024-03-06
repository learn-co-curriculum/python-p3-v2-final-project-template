from models.__init__ import CONN, CURSOR

class Member:
    all = []

    def __init__(self, name, tag):
        self.name = name
        self.tag = tag
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
    

        

    
    def arcade(self):
        return [arcade for arcade in Arcade.all if arcade.member == self]

    def locations(self):
        return list({arcade.location for arcade in self.arcade()})
    
    def __repr__(self):
        return f' Member name= "{self.name}" tag= "{self.tag}" '
    
    
    @classmethod
    def create_table(cls): 
        sql = """ 
            CREATE TABLE IF NOT EXISTS members(
            id INTEGER PRIMARY KEY,
            member TEXT,
            tag_name TEXT
            );
            """
        CURSOR.execute(sql)
        CONN.commit()
    
    # @classmethod
    # def get_all(cls):
    #     sql = " SELECT * FROM members; "
    #     print(CURSOR.execute(sql).fetchall())
    # @classmethod
    # def add_to_table(cls):
    #     sql = "INSERT INTO members "
             

    
   