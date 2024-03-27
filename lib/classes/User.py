from . import CURSOR, CONN
#import click
from classes.Visit import Visit


class User:
    
    current_user = None

    def __init__(self, name, id = None):
        self.name = name
        self.id = id
    def __repr__(self):
        return f"User ID: {self.id}  || User Name: {self.name}"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # =>    PROPERTIES    <=  # # # # # # # # # # # # # #



    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError('Name must be a string')
        elif not (len(name) >= 1 and len(name) <= 20):
            raise ValueError('Name must be between 1 and 20 characters')
        else:
            self._name = name
        # Add validation so that no users have the same name

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        if hasattr(self, 'id'):
            raise AttributeError('You are not allowed to change the id')
        else:
            self._id = id



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # => INSTANCE METHODS <=  # # # # # # # # # # # # # #
    


    # = = = = = = = = = = = = = => CRUD Methods   <= = = = = = = = = = = = = #

    def save(self):
        sql = """ 
            INSERT INTO users (name, id)
            VALUES(?, ?)
        """
        try:
            CURSOR.execute(sql, (self.name, self.id))
            CONN.commit()
            self._id = CURSOR.lastrowid
        except Exception as e:
            print('An Error Occurred:', e)
            raise Exception
        
        return self
    
    def update(self):
        sql = """
            UPDATE users
            SET name = ?
            WHERE id = ?
        """
        try:
            CURSOR.execute(sql, (self.name, self.id))
            CONN.commit()
        except Exception as e:
            print('An Error Occurred:', e)
            raise Exception

    def delete(self):
        sql = """ 
            DELETE FROM users
            WHERE id = ?
        """
        try:
            CURSOR.execute(sql, (self.id,))
            CONN.commit()
        except Exception as e:
            print('An Error Occurred:', e)
            raise Exception
        
    

    # = = = = = = = = = = = = = =>  Association Methods   <= = = = = = = = = = = #

    def visits(self):
        sql = """ 
            SELECT *
            FROM visits
            WHERE user_id = ?
        """
        try:
            CURSOR.execute(sql, (self.id,))
            CONN.commit()
            rows = CURSOR.fetchall()
            return [ Visit(row[1],row[2],row[3],row[4],row[5],row[0]) for row in rows]
        except Exception as e:
            print('An Error Occurred:', e)
            raise Exception


        


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # =>  CLASS METHODS   <=  # # # # # # # # # # # # # # 
    
    # = = = = = = = = = = = = = => CRUD Methods   <= = = = = = = = = = = = = #

    @classmethod
    def create(cls, name, id = None):
        new_user = cls(name, id)
        new_user.save()
        return new_user

    @classmethod
    def instance_from_db(cls, row):
        return cls(
            row[1], #name
            row[0]  #id
        )
    
    @classmethod
    def get_all(cls, limit=None, offset=None):
        try:
            query = 'SELECT * FROM users'
            if limit is not None and offset is not None:
                query += f' LIMIT {limit} OFFSET {offset}'
            CURSOR.execute(query)
            rows = CURSOR.fetchall()
            return [cls(row[1], row[0]) for row in rows]
        except Exception as e:
            CONN.rollback()
            print('An Error Occurred: ', e)
            raise Exception

    @classmethod
    def get_user_by_id(cls, id):
        try:
            query = 'SELECT * FROM users WHERE id = ?'
            CURSOR.execute(query, (id,))
            obj = CURSOR.fetchone()
            return cls(obj[1], obj[0])
        except Exception as e:
            CONN.rollback()
            print('An Error Occured: ', e)
            raise Exception
        
    @classmethod
    def get_user_by_name(cls, name):
        try:
            query = 'SELECT * FROM users WHERE name = ?'
            CURSOR.execute(query, (name,))
            obj = CURSOR.fetchone()
            return cls(obj[1], obj[0])
        except Exception as e:
            CONN.rollback()
            print('An Error Occured: ', e)
            raise Exception
        
    @classmethod
    def set_current_user(cls, user):

        if not cls.current_user:
            cls.current_user = user
        else:
            print('User already logged in')
            click.pause()

    # = = = = = = = = = = = = = => Table Methods   <= = = = = = = = = = = = = #
    
    @classmethod
    def create_table(cls):
        try:
            sql = """ 
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                );

            """
            CURSOR.execute(sql)
            CONN.commit()
        
        except Exception as e:
            print('An Error Occurred:', e)
            raise Exception
        
    @classmethod
    def drop_table(cls):
        try:
            sql = """ 
                DROP TABLE IF EXISTS users;
            """
            CURSOR.execute(sql)
            CONN.commit()
        except Exception as e:
            print('An Error Occurred:', e)
            raise Exception

