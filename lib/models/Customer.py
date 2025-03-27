from models.__init__ import CONN, CURSOR
import ipdb

class Customer():
    def __init__(self, name, age, id=None):
        self._id = id
        self.name = name
        self.age = age
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name has to be a string")
        if not (1 <= len(value) <= 10): 
            raise ValueError("Name has to be from 1-10 characters")
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age has to be of type int")
        if not (1 <= value <= 122):
            raise ValueError("Enter a valid age")
        self._age = value

    def save(self):
        sql = """
            INSERT INTO customer (name, age)
            VALUES (?, ?);
        """
        
        CURSOR.execute(sql, (self.name, self.age))
        CONN.commit()
    
        self._id = CURSOR.lastrowid

    def update(self):
        sql = """
            UPDATE customer
            SET name = ?, age = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.age, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM customer
            WHERE id = ?;
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self._id = None

        

    @classmethod
    def instance_from_row(cls, row):
        return cls(name=row[1], age=row[2], id=row[0])

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM customer;
        """

        customer_rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_row(row) for row in customer_rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM customer
            WHERE id = ?;
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return cls.instance_from_row(row)
        else:
            return None

    @classmethod
    def create(cls, name, age):
        new_customer = cls(name=name, age=age)
        new_customer.save()
        return new_customer

    @classmethod
    def delete_all(cls):
        sql = """
            DELETE FROM customer;
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customer (
               id INTEGER PRIMARY KEY,
               name TEXT,
               age INTEGER
            );
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS customer;"

        CURSOR.execute(sql)
        CONN.commit()

    def __repr__(self):
        return f'<customer id={self.id} name={self.name} age={self.age}>'