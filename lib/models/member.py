from models.__init__ import CURSOR, CONN

class Member:
    all = []
    def __init__(self, first_name, last_name, membership_type="Basic", id=None):
        self.id = id
        self._first_name = first_name
        self._last_name = last_name
        self._membership_type = membership_type
        Member.all.append(self)
        # self.classes_attended = [] 

    @property 
    def first_name(self):
        return self._first_name 
    
    @first_name.setter 
    def first_name(self, first_name):
        if isinstance(first_name, str) and len(first_name) > 0 and not hasattr(self, 'first_name'):
            self._first_name = first_name
        else:
            raise Exception("first name needs to be of type string and greater than 0 characters long.")

    @property 
    def last_name(self):
        return self._last_name 
    
    @last_name.setter 
    def last_name(self, last_name):
        if isinstance(last_name, str) and len(last_name) > 0 and not hasattr(self, 'last_name'):
            self._last_name = last_name
        else:
            raise Exception("last name needs to be of type string and greater than 0 characters long.")

    @property 
    def membership_type(self):
        return self._membership_type 
    
    @membership_type.setter 
    def membership_type(self, value):
        if value.lower() in ["basic", "premium"]:
            self._membership_type = value
        else:
            raise Exception("membership_type be either basic or premium.")

    @classmethod 
    def create_table(cls):
        query = """
            CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY, 
            first_name TEXT, 
            last_name TEXT, 
            membership_type TEXT);
        """
        CURSOR.execute(query)
        CONN.commit()

    @classmethod 
    def drop_table(cls):
        query = """
            DROP TABLE IF EXISTS members;
        """
        CURSOR.execute(query)
        CONN.commit()

    def save(self):
        query = """
            INSERT INTO members (first_name, last_name, membership_type)
            VALUES (?, ?, ?);
        """
        CURSOR.execute(query, (self.first_name, self.last_name, self.membership_type,))
        CONN.commit()
        self.id = CURSOR.lastrowid 

    # @classmethod 
    # def create_member_row(cls, id, first_name, last_name, membership_type="Basic"):
    #     member = cls(id, first_name, last_name, membership_type)
    #     member.save()
    #     return member 
    
    @classmethod 
    def new_member_db(cls, row):
        member = cls (
                id = row[0],
                first_name = row[1],
                last_name = row[2],
                membership_type = row[3]
            )
        print(member.first_name, member.last_name, member.membership_type)
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
        return cls(
            id = row[0],
            first_name = row[1],
            last_name = row[2],
            membership_type = [3]
        )

    # def upgrade_membership(self):
    #     if self._membership_type == "Basic":
    #         self._membership_type = "Premium"
    #         print(f"{self._first_name} {self._last_name}'s membership upgraded to Premium.")

    # def attend_class(self, exercise):
    #     self.classes_attended.append(exercise)
    #     print(f"{self.name} attended {exercise.name} class.")

    # def display_info(self):
    #     membership_info = f"Membership Type: {self.membership_type}"
    #     classes_info = f"Classes Attended: {', '.join([exercise.name for exercise in self.classes_attended])}"

    #     print(f"Member Name: {self.name}\n{membership_info}\n{classes_info}")

