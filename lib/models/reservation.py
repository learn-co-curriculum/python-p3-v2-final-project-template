from models.__init__ import CURSOR, CONN


class Reservation:

    all = {}

    def __init__(self, phone_number, length_of_stay, hotel_room_number, id=None):
        self.id = id
        self.phone_number = phone_number
        self.length_of_stay = length_of_stay
        self.hotel_room_number = hotel_room_number

    def __repr__(self):
        return (
            f"<Reservation ID: {self.id}, "
            + f"Phone: {self.phone_number}, "
            + f"Length of Stay: {self.length_of_stay}, "
            + f"Hotel Room: {self.hotel_room_number}\n>"
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
    def length_of_stay(self):
        return self._length_of_stay
    
    @length_of_stay.setter
    def length_of_stay(self, length_of_stay):
        if (
            isinstance(length_of_stay, int)
            and 0 < length_of_stay < 15
        ):
            self._length_of_stay = length_of_stay
        else:
            raise ValueError(
                "Length of stay must be an integer between 1-14"
            )
    
    @property
    def hotel_room_number(self):
        return self._hotel_room_number
    
    @hotel_room_number.setter
    def hotel_room_number(self, hotel_room_number):
        if (
            isinstance(hotel_room_number, int)
            and 0 < hotel_room_number < 11
        ):
            self._hotel_room_number = hotel_room_number
        else:
            raise ValueError(
                "Hotel Room Number must be an integer between 1-10"
            )
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of reservation instances """
        sql = """
            CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY,
            phone_number INTEGER,
            length_of_stay INTEGER,
            hotel_room_number INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists reservation instances """
        sql = """
            DROP TABLE IF EXISTS reservations;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the phone, length of stay, and hotel room values of the current reservation object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO reservations (phone_number, length_of_stay, hotel_room_number)
                VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.phone_number, self.length_of_stay, self.hotel_room_number))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Reservation instance."""
        sql = """
            UPDATE reservations
            SET phone_number = ?, length_of_stay = ?, hotel_room_number = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.phone_number, self.length_of_stay, self.hotel_room_number, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current reservation instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM reservations
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, phone_number, length_of_stay, hotel_room_number):
        """ Initialize a new reservation instance and save the object to the database """
        reservation = cls(phone_number, length_of_stay, hotel_room_number)
        reservation.save()
        return reservation
    
    @classmethod
    def instance_from_db(cls, row):
        """Return an reservation object having the attribute values from the table row."""

        # Check the dictionary for existing instance using the row's primary key
        reservation = cls.all.get(row[0])
        if reservation:
            # ensure attributes match row values in case local instance was modified
            reservation.phone_number = row[1]
            reservation.length_of_stay = row[2]
            reservation.hotel_room_number = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            reservation = cls(row[1], row[2], row[3])
            reservation.id = row[0]
            cls.all[reservation.id] = reservation
        return reservation
    
    @classmethod
    def get_all(cls):
        """Return a list containing one reservation object per table row"""
        sql = """
            SELECT *
            FROM reservations
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return reservation object corresponding to the table row matching the specified primary key"""

        sql = """
            SELECT *
            FROM reservations
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_phone(cls, phone_number):
        """Return reservation object corresponding to first table row matching specified phone_number"""
        sql = """
            SELECT *
            FROM reservations
            WHERE phone_number is ?
        """

        row = CURSOR.execute(sql, (phone_number,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
        




