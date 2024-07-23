from models.__init__ import CURSOR, CONN

class Owner:

    all = {}
    
    def __init__(self, name, phone_number, address, id=None):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.address = address

    def __repr__(self):
        return (
            f"<Owner {self.id}: {self.name}, " +
            f"Phone: {self.phone_number}, " +
            f"Address: {self.address}\n>"
        )

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if (
            isinstance(name, str) 
            and 0 < len(name) <= 20
        ):
            self._name = name
        else:
            raise ValueError(
                "Name must be a valid string between 1-20 characters"
            )
    
    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number):
        if (
            isinstance(phone_number, int) 
            and len(str(phone_number)) == 10
        ):
            self._phone_number = phone_number
        else:
            raise ValueError("Phone number must be 10 digits with no spaces")

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self,address):
        if (
            isinstance(address, str)
            and 0 < len(address)
        ):
            self._address = address
        else:
            raise ValueError("Address must be a string")
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Owner instances """
        sql = """
            CREATE TABLE IF NOT EXISTS owners (
            id INTEGER PRIMARY KEY,
            name TEXT,
            phone_number INTEGER,
            address TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Owner instances """
        sql = """
            DROP TABLE IF EXISTS owners;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, phone, and address values of the current Owner object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO owners (name, phone_number, address)
                VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.phone_number, self.address))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Owner instance."""
        sql = """
            UPDATE owners
            SET name = ?, phone_number = ?, address = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.phone_number, self.address, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Owner instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM owners
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, phone_number, address):
        """ Initialize a new Owner instance and save the object to the database """
        owner = cls(name, phone_number, address)
        owner.save()
        return owner
    
    @classmethod
    def instance_from_db(cls, row):
        """Return an Owner object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        owner = cls.all.get(row[0])
        if owner:
            # ensure attributes match row values in case local instance was modified
            owner.name = row[1]
            owner.phone_number = row[2]
            owner.address = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            owner = cls(row[1], row[2], row[3])
            owner.id = row[0]
            cls.all[owner.id] = owner
        return owner
    
    @classmethod
    def get_all(cls):
        """Return a list containing one Owner object per table row"""
        sql = """
            SELECT *
            FROM owners
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Owner object corresponding to the table row matching the specified primary key"""

        sql = """
            SELECT *
            FROM owners
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Owner object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM owners
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_phone(cls, phone_number):
        """Return owner object corresponding to first table row matching specified phone_number"""
        sql = """
            SELECT *
            FROM owners
            WHERE phone_number is ?
        """

        row = CURSOR.execute(sql, (phone_number,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def get_cats(self):
        """Return cat objects corresponding to current Owner instance"""
        from models.cat import Cat

        sql = """
            SELECT * 
            FROM cats
            WHERE owner_id = ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Cat.instance_from_db(row) for row in rows] if rows else None 


