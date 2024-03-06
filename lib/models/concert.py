
from concert_band import ConcertBand
from __init__ import CURSOR, CONN
from utils import custom_property, SQL_drop_table

def nonempty_str(value): 
    return (isinstance(value, str) and value != "")

def name_conds(name):
    if not nonempty_str(name):
        raise Error("Name must be a nonempty string.")
    return True

def date_conds(date):
    if not nonempty_str(date):
        raise Error("Date must be a nonempty string.")
    return True

# def city_conds(city):
#     if not isinstance(city, City):
#         raise TypeError("City ")
#     return True

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

    def __init__(self, name, date, bands, city, ticket_cost, id=None):
        # might do a different way so the user doesn't have the option to provide an id
        self.name = name
        self.date = date
        self.bands = bands
        self.city = city
        self.ticket_cost = ticket_cost #dict stored as string. if getting str from table, use eval() to turn back to dict
        self.id = id

    name = custom_property(name_conds)
    date = custom_property(date_conds)
    ticket_cost = custom_property(ticket_cost_conds)

    @property
    def bands(self):
        return self._bands

    @bands.setter
    def bands(self, bands):
        from band import Band
        band_objs = []
        for entry in bands:
            if isinstance(entry, Band):
                band_objs.append(entry)
                # print(f"Entry {entry} is not a band object.")
            elif isinstance(entry, str):
                instance = Band.find_by_name(entry)
                if not instance:
                    #     createBandEntry = input(f"There is no band by the name {entry}. Would you like to create one? y/n")
                    from band import Band
                    band = Band(f'{entry}')
                    # this seems okay to do because as of now bands only have a name field
                    print(f"There is no band by the name {entry}, so one was created.")
                    # raise ValueError(f"There is no band by the name {entry}. Create one before assigning it to a concert.")
                band_objs.append(instance)
            elif isinstance(band, int):
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
    def city(self, city):
        from city import City
        if isinstance(city, City):
            self._city = city
        elif isinstance(city, str):
            instance = City.find_by_name(city)
            if instance:
                self._city = instance
            else:
                raise ValueError(f"There is no city with the name {city}. Create one before assigning it to a concert.")
        elif isinstance(city, int):
            instance = City.find_by_id(city)
            if instance:
                self._city = instance
            else:
                raise ValueError(f"There is no city with the id {city}.")

    @staticmethod
    def create_table():
        sql = """
            CREATE TABLE IF NOT EXISTS concerts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            date TEXT,
            city TEXT,
            ticket_cost TEXT
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    drop_table = SQL_drop_table("concerts")

    def saveBands(self):
        # for band in self.bands:
        #     ConcertBand.create(self.id, band.id)
        [ConcertBand.create(self, band) for band in self.bands]

    def save(self):
        sql = """
                INSERT INTO concerts (name, date,  city, ticket_cost)
                VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.date, self.city.name, str(self.ticket_cost))) #will use id instead of name for city later
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).working_insts[self.id] = self

        self.saveBands() # this will make a row in concerts_bands for each pairing of self with a band

        # link_sql = """
        #     INSERT INTO concerts_bands (concert_id, band_id)
        #     VALUES (?, ?)
        # """
        # CURSOR.execute(link_sql, (self.id, ))
        
    @classmethod
    def create(cls, name, date, bands, city, ticket_cost):
        concert = cls(name, date, bands, city, ticket_cost)
        concert.save()
        return concert
    
    @classmethod
    def instance_from_db(cls, row):
        concert = cls.working_insts.get(row[0])
        if concert:
            concert.name = row[1]
            concert.date = row[2]
            concert.bands = row[3]
            concert.city = row[4]
            concert.ticket_cost = row[5]
            # could maybe  use something concert.__dict__.values() = [*row] but dict is unordered
        else:
            bands = ConcertBand.get_all_bands_by_concert_id(row[0])
            concert = cls(*row[1:3], bands, *row[4:]) #using list unpacking *
            concert.id = row[0]
            cls.working_insts[concert.id] = concert
        return city

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM concerts
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None