from models.__init__ import (CONN, CURSOR)
from models.player import Player

class Pet:

    all_pets = {}

    def __init__(self, name, species, age, owner_id):
        self.name = name
        self.species = species
        self.age = age
        self.owner_id = owner_id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Name must be a string with more than 3 characters.")
        
    @property
    def species(self):
        return self._species
    
    @species.setter
    def species(self, species):
        if isinstance(species, str):
            self._species = species
        else:
            raise ValueError("This species is not supported yet!")
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age >= 0:
            self._age = age
        else:
            raise ValueError("Age must be higher than or equal to 0.")
        
    @property
    def owner_id(self):
        return self._owner_id
    
    @owner_id.setter
    def owner_id(self, owner_id):
        if isinstance(owner_id, int):
            self._owner_id = owner_id
        else:
            raise TypeError("Owner_id must be a number.")

    def __repr__(self) -> str:
        return f"<Pet {self.name} - {self.species} - {self.age}>"
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Pet instances """
        sql = """
            CREATE TABLE pets (
                id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                age INTEGER,
                owner_id INTEGER,
                FOREIGN KEY (owner_id) REFERENCES players(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop Player table """
        sql = """
            DROP TABLE IF EXISTS pets
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the attribute values of the current Pet instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO pets (name, species, age, owner_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.species, self.age, self.owner_id))
        CONN.commit()

        # Assign the id of the instance to be the table's last row id:
        self.id = CURSOR.lastrowid

        # Saves the instance to the "all_pets" dictionary:
        type(self).all_pets[self.id] = self

    @classmethod
    def create(cls, name, species, age, owner_id):
        """ Initialize a new Pet instance and save the object to the database """
        pet = cls(name, species, age, owner_id)
        pet.save()
        return pet
    
    def update(self):
        """Update the table row corresponding to the current Pet instance."""
        sql = """
            UPDATE players
            SET name = ?, species = ?, age = ?, owner_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.species, self.age, self.owner_id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Player instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM pets
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all_pets[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Pet object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        pet = cls.all_pets.get(row[0])
        if pet:
            # ensure attributes match row values in case local instance was modified
            pet.name = row[1]
            pet.species = row[2]
            pet.age = row[3]
            pet.owner_id = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            pet = cls(row[1], row[2], row[3], row[4])
            pet.id = row[0]
            cls.all_pets[pet.id] = pet
        return pet

    @classmethod
    def get_all(cls):
        """Return a list containing a Pet object per row in the table"""
        sql = """
            SELECT *
            FROM pets
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Pet object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM pets
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Pet object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM pets
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None