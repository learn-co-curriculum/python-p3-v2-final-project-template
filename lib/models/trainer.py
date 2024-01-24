from models.__init__ import CURSOR, CONN

class Trainer:

    all = {}

    def __init__(self, first_name, last_name, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self):
        return f"<Trainer {self.id}: {self.first_name} {self.last_name}>"
    
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str) and 0 < len(value):
            self._first_name = value
        else:
            raise Exception("first name needs to be of type string and greater than 0 characters long.")
    
    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, value):
        if isinstance(value, str) and 0 < len(value):
            self._last_name = value
        else:
            raise Exception("last name needs to be of type string and greater than 0 characters long.")

    @classmethod
    def create_table(cls):
        query = """
            CREATE TABLE IF NOT EXISTS trainers (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT
            );
        """
        CURSOR.execute(query)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        query = """
            DROP TABLE IF EXISTS trainers;
        """
        CURSOR.execute(query)
        CONN.commit()

    #instance method / not class method
    def save(self):
        query = """
            INSERT INTO trainers (first_name, last_name)
            VALUES (?, ?);
        """
        CURSOR.execute(query, (self.first_name, self.last_name))
        CONN.commit() #save the changes
        self.id = CURSOR.lastrowid #update the id
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, first_name, last_name):
        trainer = cls(first_name, last_name)
        trainer.save()

        return trainer
    
    def update(self):
        sql = """
            UPDATE trainers
            SET first_name = ?, last_name = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.first_name, self.last_name, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM trainers
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        trainer = cls.all.get(row[0])

        if trainer:
            trainer.first_name = row[1]
            trainer.last_name = row[2]

        else:
            trainer = cls(row[1], row[2])
            trainer.id = row[0]
            cls.all[trainer.id] = trainer

        return trainer
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM trainers
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        return cls.instance_from_db(row) if row else None
    
    # @classmethod
    # def get_all(cls):
    #     sql = """
    #         SELECT * FROM trainers;
    #     """
    #     CURSOR.execute(sql)
    #     rows = CURSOR.fetchall()
    #     trainers = []
    #     for row in rows:
    #         trainer = cls.new_form_db(row)
    #         trainers.append(trainer)
    #     return trainers
    