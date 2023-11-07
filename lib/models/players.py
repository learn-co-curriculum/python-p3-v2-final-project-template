import sqlite3
CONN = sqlite3.connect('dnd_data.sqlite')
CURSOR = CONN.cursor()

# import ipdb

class Player:
    def __init__(self, name, password, age, next_game=False, id=None):
        self.id = id
        self.name = name
        self.password = password
        self.age = age
        self.next_game = next_game
    
    def __repr__(self):
        return f'Player: {self.name}, Age: {self.age}'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) == str:
            self._name = new_name
        else:
            raise ValueError('Name must be string!')
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, new_password):
        if type(new_password) == str:
            if len(new_password) >= 5:
                self._password = new_password
            else:
                raise ValueError('Password must be at least 5 characters!')
        else:
            raise ValueError('Password must be string!')
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if type(new_age) == int:
            if new_age >= 18:
                self._age = new_age
            else:
                raise ValueError('Age must be 18 or greater!')
        else:
            raise ValueError('Age must be an integer!')

    def save(self):
        sql = """
            INSERT INTO players (name, password, age, next_game) 
            VALUES (?, ?, ?, ?);
        """
        var_tuple = (self.name, self.password, self.age, self.next_game)
        CURSOR.execute(sql, var_tuple)
        CONN.commit()

        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, password, age, next_game):
        player = Player(name, password, age, next_game)
        player.save()
        return player
    
    def characters(self):
        sql = """
            SELECT * FROM characters WHERE player = ?
        """
        var_tuple = self.id
        result = CURSOR.execute(sql, var_tuple).fetchall()
        return result

    @classmethod
    def all(cls):
        sql = """
            SELECT * FROM players;
        """
        players = CURSOR.execute(sql).fetchall()
        return [Player(player[1], player[2], player[3], player[4], player[0]) for player in players]

    @classmethod
    def next_players(cls):
        sql = """
            SELECT * FROM players WHERE next_game = 1;
        """
        players = CURSOR.execute(sql).fetchall()
        return [Player(player[1], player[2], player[3], player[4], player[0]) for player in players]
    
    @classmethod
    def reset_next(cls):
        sql = """
            UPDATE players SET next_game = False;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM players WHERE id = ?;
        """
        var_tuple = (self.id,)
        CURSOR.execute(sql,var_tuple)
        CONN.commit()
        self.id = None
    
    def update(self):
        sql = """
            UPDATE players 
            SET name = ?, password = ?, age = ?, next_game = ?
            WHERE id = ?;
        """
        var_tuple = (self.name, self.password, self.age, self.next_game, self.id)
        CURSOR.execute(sql, var_tuple)
        CONN.commit()
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM players WHERE name = ?;
        """
        var_tuple = (name,)
        players = CURSOR.execute(sql, var_tuple).fetchall()
        return [Player(player[1], player[2], player[3], player[4], player[0]) for player in players]

# ipdb.set_trace()