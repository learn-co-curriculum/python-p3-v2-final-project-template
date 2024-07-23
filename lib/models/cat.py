from models.__init__ import CURSOR, CONN
from models.owner import Owner

ACCEPTED_BREEDS = [
    "tabby",
    "calico",
    "shorthair",
    "siamese",
    "maine coon",
    "persian",
    "ragdoll",
    "sphynx",
    "scottish fold",
]


class Cat:
    all = {}

    def __init__(self, name, breed, age, spice_level, owner_id, id=None):
        self.id = id
        self.name = name
        self.breed = breed
        self.age = age
        self.spice_level = spice_level
        self.owner_id = owner_id

    def __repr__(self):
        return (
            f"<Cat ID: {self.id}, " +
            f"Name: {self.name}, " +
            f"Breed: {self.breed}, " +
            f"Age: {self.age}, " +
            f"Spice Level: {self.spice_level}, " +
            f"Owner Id: {self.owner_id}\n>"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 0 < len(name) <= 30:
            self._name = name
        else:
            raise ValueError("Name must be non-empty string of 30 or fewer characters")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        if ACCEPTED_BREEDS.count(breed) > 0:
            self._breed = breed
        else:
            raise ValueError("Cat breed must be on the approved list of breeds")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int) and 0 < age <= 30:
            self._age = age
        else:
            raise ValueError("Age must be an integer between 0 and 30 years")

    @property
    def spice_level(self):
        return self._spice_level

    @spice_level.setter
    def spice_level(self, spice_level):
        if isinstance(spice_level, int) and 1 <= spice_level <= 5:
            self._spice_level = spice_level
        else:
            raise ValueError("Spice level must be an integer from one to five")

    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        if isinstance(owner_id, int) and Owner.find_by_id(owner_id):
            self._owner_id = owner_id
        else:
            raise ValueError(" owner_id must reference an owner in the database")

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Cat instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS cats (
            id INTEGER PRIMARY KEY,
            name TEXT,  
            breed TEXT, 
            age INTEGER, 
            spice_level INTEGER,
            owner_id INTEGER,
            FOREIGN KEY (owner_id) REFERENCES owners(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists cats instances"""
        sql = """
            DROP TABLE IF EXISTS cats;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the values of the current Cat object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO cats (name, breed, age, spice_level, owner_id)
                VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(
            sql, (self.name, self.breed, self.age, self.spice_level, self.owner_id)
        )
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Cat instance."""
        sql = """
            UPDATE cats
            SET name = ?, breed = ?, age = ?, spice_level = ?, owner_id = ?
            WHERE id = ?
        """
        CURSOR.execute(
            sql,
            (
                self.name,
                self.breed,
                self.age,
                self.spice_level,
                self.owner_id,
                self.id,
            ),
        )
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Cat instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM cats
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, breed, age, spice_level, owner_id):
        """Initialize a new Cat instance and save the object to the database"""
        cat = cls(name, breed, age, spice_level, owner_id)
        cat.save()
        return cat

    @classmethod
    def instance_from_db(cls, row):
        """Return an Cat object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        cat = cls.all.get(row[0])
        if cat:
            # ensure attributes match row values in case local instance was modified
            cat.name = row[1]
            cat.breed = row[2]
            cat.age = row[3]
            cat.spice_level = row[4]
            cat.owner_id = row[5]
        else:
            # not in dictionary, create new instance and add to dictionary
            cat = cls(row[1], row[2], row[3], row[4], row[5])
            cat.id = row[0]
            cls.all[cat.id] = cat
        return cat

    @classmethod
    def get_all(cls):
        """Return a list containing one Cat object per table row"""
        sql = """
            SELECT *
            FROM cats
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Cat object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM cats
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_owner(cls, owner_id):
        """Return list of cats corresponding to the table rows matching the owner ID"""
        sql = """
            SELECT *
            FROM owners
            WHERE owner_id is ?
        """

        rows = CURSOR.execute(sql, (owner_id,)).fetchall()
        return [Cat.instance_from_db(row) for row in rows] if rows else None

    def owner(self):
        """Return cat's owner"""
        from models.owner import Owner

        sql = """
            SELECT * FROM owners
            WHERE id= ?
        """
        CURSOR.execute(
            sql,
            (self.owner_id,),
        )

        row = CURSOR.execute(sql, (self.owner_id,)).fetchone()
        return Owner.instance_from_db(row) if row else None
