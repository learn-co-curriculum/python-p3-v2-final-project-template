from models.__init__ import CONN, CURSOR

class User:
    def __init__(self, name, score=0, id=None):
        self.name = name
        self.score = score
        self.id = id

    def __repr__(self):
        return f"Player {self.id}: {self.name}"

    #! Properties

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        elif len(new_name) < 3:
            raise ValueError("Name must be 3 or more characters")
        else:
            self._name = new_name

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if not isinstance(new_score, int):
            raise TypeError("Score must be an integer")
        elif new_score < 0:
            raise ValueError("Score cannot be less than 0")
        else:
            self._score = new_score

    #! Attributes


    #! ORM class methods

    @classmethod
    def create_table(cls):
        CURSOR.execute(
            """
                CREATE TABLE IF NOT EXISTS players (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    score INTEGER
                );
            """
        )
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute(
            """
                DROP TABLE IF EXISTS players;
            """
        )
        CONN.commit()

    @classmethod
    def create(cls, name):
        new_player = cls(name)
        new_player.save()
        return new_player

    @classmethod
    def get_all(cls):
        CURSOR.execute(
            """
                SELECT * from players;
            """
        )
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[0]) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute(
            """
                SELECT * FROM players
                WHERE name is ?;
            """,
            (name,)
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[0]) if row else None
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute(
            """
                SELECT * FROM players
                WHERE id is ?;
            """,
            (id,)
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[0]) if row else None

    #! ORM instance methods

    def save(self):
        CURSOR.execute(
            """
                INSERT INTO players (name, score)
                VALUES (?, ?)
            """,
            (self.name, self.score)
        )
        CONN.commit()
        self.id = CURSOR.lastrowid
        return self
    
    def update(self):
        CURSOR.execute(
            """
                UPDATE players
                SET name = ?, score = ?
                WHERE id = ?
            """,
            (self.name, self.score, self.id)
        )
        CONN.commit()
        return self
    
    def delete(self):
        CURSOR.execute(
            """
                DELETE FROM players
                WHERE id = ?
            """,
            (self.id,)
        )
        CONN.commit()
        self.id = None
        return self

