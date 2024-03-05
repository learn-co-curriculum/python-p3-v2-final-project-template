class Concert:
    all = []

    def __init__(self, name, date, band, city, ticket_cost):
        self.name = name
        self.date = date
        self.band = band
        self.city = city
        self.ticket_cost = ticket_cost  

        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date) > 0:
            self._date = date
        else:
            raise ValueError("Date must be a non-empty string")

    @property
    def ticket_cost(self):
        return self._ticket_cost

    @ticket_cost.setter
    def ticket_cost(self, ticket_cost):
        if isinstance(ticket_cost, dict):
            for ticket_type, details in ticket_cost.items():
                if not isinstance(ticket_type, str):
                    raise TypeError("Ticket type must be a string")
                if not (isinstance(details, list) and len(details) == 2):
                    raise TypeError("Details must be a list with two elements: cost and attendance")
                cost, attendance = details
                if not (isinstance(cost, (int, float)) and cost >= 0):
                    raise ValueError("Cost must be a non-negative number")
                if not (isinstance(attendance, int) and attendance >= 0):
                    raise ValueError("Attendance must be a non-negative integer")
            self._ticket_cost = ticket_cost
        else:
            raise TypeError("Ticket cost must be a dictionary")

        
        
         #concert band 
        #must be of type band
        #should be able ti change after the cocert is instantiated

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, band):
       from models.band import Band
       if isinstance(band, Band):
           self._band + band 
       else :
            raise Exception("Band must be an instrance of Band class!")
   

    def home_city_show(self):
        return f"The band {self.band.name} is playing a show in their home city, {self.band.home_city}, at {self.city} on {self.date}."
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Concert instances """
        sql = """
            CREATE TABLE IF NOT EXISTS concerts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            date TEXT,
            band TEXT,
            city TEXT,
            ticket_cost FLOAT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persisits Concert instances """
        sql = """
            DROP TABLE IF EXISTS concerts;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, date, band, city and ticket_cost values of the current Concert object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO concerts (name, date, band, city, ticket_cost)
                VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self,date, self.band, self.city, self.ticket_cost))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Concert instance."""
        sql = """
            UPDATE concerts
            SET name = ?, date = ?, band = ?, city = ?, ticket_cost = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.date, self.band, self.city, self.ticket_cost))
        CONN.commit()

    def delete(self):
        """ Delete the table row corresponding to the current Concert instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM concerts
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # delete the dictionary entry using id as the key
        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """ Return Concert object having the attribute values from the table row."""

        concert = cls.all.get(row[0])
        if concert:
            concert.name = row[1]
            concert.date = row[2]
            concert.band = row[3]
            concert.city = row[4]
            concert.ticket_cost = row[5]
        else:
            concert = cls(row[1],row[2], row[3],row[4],row[5])
            concert.id = row[0]
            cls.all[concert.id] = concert
        return concert

    @classmethod
    def get_all(cls):
        """ Return a list containing a Concert object per row in the table """
        sql = """
            SELECT *
            FROM departments
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """ Return a Concert object corresponding to the table row matching the specified primary key """
        sql = """
            SELECT * 
            FROM concerts
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod 
    def find_ny_name(cls, name):
        """ Return a Concert object corresponding to the first table row matching specified name """
        sql = """
            SELECT *
            FROM departments
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def bands(self):
        """ Return list of cities associated with current concert """
        from city import City
        sql = """
            SELECT * FROM cities
            WHERE name = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [City.instance_from_db(row) for row in rows]
        
