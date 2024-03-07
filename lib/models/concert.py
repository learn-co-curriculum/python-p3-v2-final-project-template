from models.__init__ import CURSOR, CONN
from models.concert_band import ConcertBand
from models.utils import punctuate_str, check_nonempty_str, custom_property, SQL_drop_table, SQL_get_all, SQL_show_all, SQL_find_by_attribute

def name_conds(name):
    check_nonempty_str(name, "Concert name")
    return True

def date_conds(date):
    check_nonempty_str(date, "Concert date")
    return True

def ticket_cost_conds(ticket_cost):
    if not isinstance(ticket_cost, dict):
        raise TypeError("Ticket cost must be a dictionary")
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
    return True
    
class Concert:

    working_insts = {}
    table_name = "concerts"

    def __init__(self, name, date, bands, city, ticket_cost, id=None):
        # might do a different way so the user doesn't have the option to provide an id
        self.name = name
        self.date = date
        self.bands = bands
        self.city = city
        self.ticket_cost = ticket_cost #dict stored as string. if getting str from table, use eval() to turn back to dict
        self.id = id

    def __str__(self):
        from datetime import datetime
        today = datetime.today()
        concert_date = datetime.strptime(self.date, f"%m/%d/%Y")
        upcoming = today.date() < concert_date.date()
        from models.band import Band
        return f"""    {self.name} (id: {self.id}) {'will happen' if upcoming else "happened"} on {self.date} in {self.city.name}!
    {punctuate_str(self.bands, True)} {"will be there." if upcoming else "were there."}
""" #this looks wonky here but it looks nice when printed

    name = custom_property(name_conds)
    date = custom_property(date_conds)
    ticket_cost = custom_property(ticket_cost_conds)

    @property
    def bands(self):
        return self._bands

    @bands.setter
    def bands(self, bands):
        from models.band import Band
        band_objs = []
        for entry in bands:
            if isinstance(entry, Band):
                band_objs.append(entry)
                # print(f"Entry {entry} is not a band object.")
            elif isinstance(entry, str):
                instance = Band.find_by_name(entry)
                if not instance:
                    #     createBandEntry = input(f"There is no band by the name {entry}. Would you like to create one? y/n")
                    # print(f"There is no band by the name {entry}, so one was created.")
                    raise ValueError(f"There is no band by the name {entry}. Create one before assigning it to a concert.")
                band_objs.append(instance)
            elif isinstance(entry, int):
                instance = Band.find_by_id(entry)
                if not instance:
                    raise ValueError(f"There is no band with the id {entry}.")
                band_objs.append(instance)
            else:
                raise TypeError("Entry {band} is not a band object, a string, or an int.")
            
        self._bands = band_objs

    @property
    def city(self):
        return self._city

    @city.setter
    #this could go in utils since the same method is in band
    def city(self, city):
        if city == None:
            print("There is no city attribute!")
            self._city = city
            return
        from models.city import City
        if isinstance(city, City):
            self._city = city
            return
        elif isinstance(city, str):
            instance = City.find_by_name(city)
            if instance:
                self._city = instance
                return
            else:
                # raise ValueError(f"There is no city with the name {city}. Create one before assigning it to a concert.")
                city_object = City.create(city)
                # this seems okay to do because as of now City instances only have a name field
                self._city = city_object
                return
        elif isinstance(city, int):
            instance = City.find_by_id(city)
            if instance:
                self._city = instance
                return
            else:
                raise ValueError(f"There is no city with the id {city}.")
        raise TypeError("city must be a City object, a string, the integer id of an existing city, or None.")

    @staticmethod
    def create_table():
        sql = """
            CREATE TABLE IF NOT EXISTS concerts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            date TEXT,
            city_id INT,
            ticket_cost TEXT,
            FOREIGN KEY (city_id) REFERENCES cities(id))
        """

        CURSOR.execute(sql)
        CONN.commit()

    drop_table = SQL_drop_table(table_name)

    def saveBands(self):
        [ConcertBand.create(self, band) for band in self.bands]

    def save(self):
        print(self.city)
        sql = """
                INSERT INTO concerts (name, date,  city_id, ticket_cost)
                VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.date, self.city.id, str(self.ticket_cost))) #will use id instead of name for city later
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).working_insts[self.id] = self

        self.saveBands() # this will make a row in concert_bands for each pairing of self with a band
        
    @classmethod
    def create(cls, name, date, bands, city, ticket_cost):
        concert = cls(name, date, bands, city, ticket_cost)
        concert.save()
        return concert

    def update(self):
        sql = f"""
            UPDATE concerts
            SET name = ?, date = ?, city_id = ?, ticket_cost = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.date, self.city.id, str(self.ticket_cost)))
        CONN.commit()
        # !!!!! update concert_bands?? 

    def get_bands(self):
        sql = """
            SELECT bands.id, bands.name, bands.members, bands.genre, bands.home_city_id
            FROM bands
            INNER JOIN concert_bands
            ON bands.id = concert_bands.band_id WHERE concert_bands.concert_id = ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        from models.band import Band
        return [Band.instance_from_db(row) for row in rows]

    def show_bands(self):
        print(f'{self.name} will be attended by:')
        for band in self.get_bands():
            print(f'    {band.name}')

    @classmethod
    def get_bands_by_id(cls, id):
        sql = """
            SELECT bands.id, bands.name, bands.members, bands.genre, bands.home_city_id
            FROM bands
            INNER JOIN concert_bands
            ON bands.id = concert_bands.band_id WHERE concert_bands.concert_id = ?
        """
        rows = CURSOR.execute(sql, (id,)).fetchall()
        from models.band import Band
        return [Band.instance_from_db(row) for row in rows]

    def show_bands(self):
        print(f'{self.name} will be attended by:')
        for band in self.get_bands():
            print(f'    {band.name}')

    
    @classmethod
    def instance_from_db(cls, row):
        concert = cls.working_insts.get(row[0])
        concert_id, name, date, city_id, ticket_cost = row
        print(concert_id)
        from models.city import City
        if concert:
            concert.name = name
            concert.date = date
            concert.bands = cls.get_bands_by_id(concert_id) # unfortunately just a row from concerts will not have the band list
            concert.city = City.find_by_id(city_id)
            concert.ticket_cost = eval(ticket_cost)
            # could maybe  use something concert.__dict__.values() = [*row] but dict is unordered
        else:
            bands = cls.get_bands_by_id(concert_id)
            concert = cls(name, date, bands, City.find_by_id(city_id), eval(ticket_cost))
            concert.id = concert_id
            cls.working_insts[concert.id] = concert
        return concert

    get_all = SQL_get_all()
    show_all = SQL_show_all()

    find_by_id = SQL_find_by_attribute("id")
    find_by_name = SQL_find_by_attribute("name")