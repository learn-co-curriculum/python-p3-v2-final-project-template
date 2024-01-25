from models.__init__ import CURSOR, CONN

class Member:

    all = {}

    def __init__(self, first_name, last_name, membership_type="Basic", id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.membership_type = membership_type

    def __repr__(self):
        return f"<Member {self.id}: {self.first_name} {self.last_name}, Membership Type: {self.membership_type}>"

    @property 
    def first_name(self):
        return self._first_name 
    
    @first_name.setter 
    def first_name(self, first_name):
        if isinstance(first_name, str) and len(first_name) > 0:
            self._first_name = first_name
        else:
            raise Exception("first name needs to be of type string and greater than 0 characters long.")

    @property 
    def last_name(self):
        return self._last_name 
    
    @last_name.setter 
    def last_name(self, last_name):
        if isinstance(last_name, str) and len(last_name) > 0:
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
            raise Exception("membership_type has to be either basic or premium.")

    def delete(self):
        if self.id is not None:
            sql = "DELETE FROM members WHERE id = ?"
            CURSOR.execute(sql, (self.id,))
            CONN.commit()
            print(f"Member with ID {self.id} - {self.first_name} {self.last_name} has been deleted from the database.")
        else:
            print("Member not found or already deleted.")

    def delete_from_all(self):
        Member.all = [member for member in Member.all if member.id != self.id]

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

    @classmethod 
    def create_member_row(cls, first_name, last_name, membership_type="Basic"):
        member = cls(first_name, last_name, membership_type)
        member.save()
        return member 

    def save(self):
        if self.id is None:
            query = """
                INSERT INTO members (first_name, last_name, membership_type)
                VALUES (?, ?, ?);
            """
            CURSOR.execute(query, (self.first_name, self.last_name, self.membership_type))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            query = """
                UPDATE members
                SET first_name = ?, last_name = ?, membership_type = ?
                WHERE id = ?;
            """
            CURSOR.execute(query, (self.first_name, self.last_name, self.membership_type, self.id))
            CONN.commit()


    @classmethod
    def create(cls, first_name, last_name, membership_type="Basic"):
        member = cls(first_name, last_name, membership_type)
        member.save()
        return member
    
    def update(self):
        sql = """
            UPDATE members
            SET first_name = ?, last_name = ?, membership_type = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.first_name, self.last_name, self.membership_type, self.id))
        CONN.commit()

    def delete(self):
        if self.id is not None:
            try:
                sql = "DELETE FROM members WHERE id = ?"
                CURSOR.execute(sql, (self.id,))
                CONN.commit()
                print(f"Member with ID {self.id} - {self.first_name} {self.last_name} has been deleted from the database.")
                del type(self).all[self.id]
                self.id = None
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Member not found or already deleted.")

    @classmethod
    def instance_from_db(cls, row):
        member = cls.all.get(row[0])

        if member:
            member.first_name = row[1]
            member.last_name = row[2]
            member.membership_type = row[3]
        
        else:
            member = cls(row[1], row[2], row[3])
            member.id = row[0]
            cls.all[member.id] = member

        return member
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM members
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        return cls.instance_from_db(row) if row else None
    
    @classmethod 
    def find_by_name(cls, first_name, last_name):
        sql = """
            SELECT * FROM members
            WHERE first_name = ? 
            AND last_name = ?
            LIMIT 1
        """
        row = CURSOR.execute(sql, (first_name, last_name)).fetchone()
        if row:
            return cls(
            id = row[0],
            first_name = row[1],
            last_name = row[2],
            membership_type = row[3]
        )
        return None
    
    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM members WHERE id = ?"
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], first_name=row[1], last_name=row[2], membership_type=row[3])
        return None
    

    @classmethod 
    def get_all(cls):
        sql = """
            SELECT * FROM members
            ORDER BY last_name, first_name
        """
        return [cls.instance_from_db(one_row) for one_row in CURSOR.execute(sql).fetchall()]
    
