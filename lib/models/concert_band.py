from  __init__ import CURSOR, CONN
from utils import custom_property, SQL_drop_table

def concert_conds(concert):
    from concert import Concert
    if isinstance(concert, Concert):
        return True
    raise TypeError("concert must be of type concert")

def band_conds(band):
    from band import Band
    if isinstance(band, Band):
        return True
    raise TypeError("band must be of type band")

class ConcertBand:

    def __init__(self, concert, band):
        self.concert = concert
        self.band = band

    concert = custom_property(concert_conds)
    band = custom_property(band_conds)

    @staticmethod
    def create_table():
        sql = """
            CREATE TABLE IF NOT EXISTS concerts_bands (
                concert_id INT,
                band_id INT,
                PRIMARY KEY
                (
                    concert_id
                    band_id
                ),
                FOREIGN KEY (concert_id) REFERENCES concerts (concert_id)
                FOREIGN KEY (band_id) REFERENCES bands (band_id)
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    drop_table = SQL_drop_table("concerts_bands")

    def save(self):
        sql = """
            INSERT INTO concerts_cities (concert_id, band_id)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.concert_id, self.band_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).working_insts[self.id] = self

    @classmethod
    def create(cls, name):
        concert_band = cls(name)
        concert_band.save()
        return concert_band

    @classmethod
    def instance_from_db(cls, row):
        concert_band = cls.working_insts.get(row[0])
        if concert_band:
            concert_band.concert_id = row[1]
            concert_band.band_id = row[2]
        else:
            # city = cls(row[1])
            # city.id = row[0]
            # i don't like making this new city object
            # and returning it as if it was in the db without adding it
            raise Error("Cannot find row")
        return concert_band

    @classmethod
    def find_by_id(cls, id):
        sql = """
        SELECT *
        FROM concerts_bands
        WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def update(self):
        sql = """
            UPDATE concerts_bands
            SET name = ?
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
            FROM cities
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]