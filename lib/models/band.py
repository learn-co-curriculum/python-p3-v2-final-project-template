from models.__init__ import CURSOR, CONN
from models.utils import punctuate_str, check_nonempty_str, custom_property, SQL_drop_table, SQL_get_all, SQL_show_all, SQL_find_by_attribute, SQL_delete

def name_conds(name):
    # the check function below has probably made things more confusing than the space it saves
    check_nonempty_str(name, "Band name")
    return True

def members_conds(members):
    if not isinstance(members, list) and members:
        raise TypeError("Members must be a non-empty list.") 
    for member in members:
        if not isinstance(member, str):
            raise TypeError("All members must be strings.")
    return True

def genre_conds(genre):
    check_nonempty_str(genre, "Genre")
    return True

class Band:

    working_insts = {}
    table_name = "bands"

    def __init__(self, name, members, genre, home_city, id=None):
        self.name = name   
        self.members = members
        self.genre = genre
        self.home_city = home_city
        self.id = id

        self.working_insts[self.id] = self

    def __str__(self): 
        return f"""    {self.name} (id: {self.id if self.id else "None"}) is from {self.home_city.name} and plays {self.genre}
    {self.name}'s {"sole member is" if len(self.members) == 1 else "members are"} {punctuate_str(self.members)}
""" #this looks wonky here but it looks nice when printed

    name = custom_property(name_conds)
    members = custom_property(members_conds)
    genre = custom_property(genre_conds)
    
    @property
    def home_city(self):
        return self._home_city

    @home_city.setter
    #this could go in utils since the same method is in concert
    def home_city(self, home_city):
        if home_city == None:
            print("There is no home_city attribute!")
            self._home_city = home_city
            return
        from models.city import City
        if isinstance(home_city, City):
            self._home_city = home_city
            return
        elif isinstance(home_city, str):
            instance = City.find_by_name(home_city)
            if instance:
                self._home_city = instance
                return
            else:
                # raise ValueError(f"There is no city with the name {city}. Create one before assigning it to a concert.")
                city_object = City.create(home_city)
                # this seems okay to do because as of now City instances only have a name field
                self._home_city = city_object
                return
        elif isinstance(home_city, int):
            instance = City.find_by_id(home_city)
            if instance:
                self._home_city = instance
                return
            else:
                raise ValueError(f"There is no city with the id {city}.")
        raise TypeError("home_city must be a City object, a string, the integer id of an existing city, or None.")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS bands (
            id INTEGER PRIMARY KEY,
            name TEXT,
            members TEXT,
            genre TEXT,
            home_city_id INTEGER,
            FOREIGN KEY (home_city_id) REFERENCES cities(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    drop_table = SQL_drop_table(table_name)

    def save(self):
        members_str = ','.join(self.members)
        sql = """
            INSERT INTO bands (name, members, genre, home_city_id)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, members_str, self.genre, self.home_city.id)) #will have to replace home city with an id
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).working_insts[self.id] = self

    @classmethod
    def create(cls, name, members, genre, home_city_id):
        band = cls(name, members, genre, home_city_id)
        band.save()
        return band

    def update(self):
        # don't go trying to change and update the id, because it won't update in the junction table
        # i'd like to not let id be reassigned at all with a setter hasattr, but i need to remove id the delete method
        members_str = ','.join(self.members)
        sql = f"""
            UPDATE bands
            SET name = ?, members = ?, genre = ?, home_city_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, members_str, self.genre, self.home_city.id, self.id))
        CONN.commit()

    def delete(self):
        #so this deleter method will let the concerts and bands with that city id have null in their table cell
        #this isn't great because null isn't an allowed value for the objects
        #delete entries from concert_bands
        sql = """
            DELETE FROM concert_bands
            WHERE band_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        #delete entry from bands and cleanup id
        SQL_delete(type(self).table_name)(self)

    @classmethod
    def instance_from_db(cls, row):
        band_id, name, members_str, genre, home_city_id = row
        members = members_str.split(',')
        band = cls.working_insts.get(band_id)
        from models.city import City
        if band:
            band.name = name
            band.members = members
            band.genre = genre
            band.home_city = City.find_by_id(home_city_id)
        else:
            band = cls(name, members, genre, City.find_by_id(home_city_id))
            band.id = band_id
        return band

    get_all = SQL_get_all()
    show_all = SQL_show_all()

    find_by_id = SQL_find_by_attribute("id")
    find_by_name = SQL_find_by_attribute("name")
    find_by_genre = SQL_find_by_attribute("genre", False) #false so fetchall is used instead of fetchone