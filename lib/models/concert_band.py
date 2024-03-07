from models.__init__ import CURSOR, CONN
from models.utils import custom_property, SQL_drop_table

#this class has a lot of methods that aren't written correctly and shouldn't be used
#it maybe shouldn't have a class itself and just be a table
#right now it is only used to make a table and for Concert.save()
#in a finished product all the concert and band methods could use this class to update the link table

def concert_conds(concert):
    from models.concert import Concert
    if isinstance(concert, Concert):
        return True
    raise TypeError("concert must be of type concert")

def band_conds(band):
    from models.band import Band
    if isinstance(band, Band):
        return True
    raise TypeError("band must be of type band")

class ConcertBand:

    def __init__(self, concert, band):
        self.concert = concert
        self.band = band

    table_name = "concert_bands"
    concert = custom_property(concert_conds)
    band = custom_property(band_conds)

    @staticmethod
    def create_table():
        sql = """
            CREATE TABLE IF NOT EXISTS concert_bands (
                concert_id INT,
                band_id INT,
                PRIMARY KEY
                (
                    concert_id,
                    band_id
                ),
                FOREIGN KEY (concert_id) REFERENCES concerts (concert_id)
                FOREIGN KEY (band_id) REFERENCES bands (band_id)
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    drop_table = SQL_drop_table(table_name)

    def save(self):
        sql = """
            INSERT INTO concert_bands (concert_id, band_id)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.concert.id, self.band.id))
        CONN.commit()

        # self.id = CURSOR.lastrowid
        # type(self).working_insts[self.id] = self

    @classmethod
    def create(cls, concert, band):
        concert_band = cls(concert, band)
    # def create(cls, concert_id, band_id):
    #     concert_band = cls(concert_id, band_id)
        concert_band.save()
        return concert_band

    @classmethod
    def instance_from_db(cls, row):
        from models.concert import Concert
        from models.band import Band
        concert_band = cls.working_insts.get(row[0])
        if concert_band:
            concert_band.concert = Concert.find_by_id(row[1])
            concert_band.band = Band.find_by_id(row[2])
        else:
            concert_band = cls(Concert.find_by_id(row[1]), Band.find_by_id(row[2]))
            # do i need to add it to a class.all here? if i did, what would the key be? (primary key is two columns)
        return concert_band

    @classmethod
    def find_by_id(cls, id):
        sql = """
        SELECT *
        FROM concert_bands
        WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def update(self):
        sql = """
            UPDATE concert_bands
            SET 
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM cities
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).working_insts[self.id]
        self.id = None

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM concert_bands
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @staticmethod
    def get_all_bands_by_concert_id(concert_id):
        # need this method for Concert.instance_from_db
        sql = """
        SELECT band_id
        FROM concert_bands
        WHERE concert_id = ?
        """
        band_ids = CURSOR.execute(sql, (concert_id,)).fetchall()
        
        from models.band import Band
        return [Band.find_by_id(band_id).name for band_id in band_ids]