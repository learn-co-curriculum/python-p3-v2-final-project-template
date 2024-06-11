from models.__init__ import CONN, CURSOR

class BorrowingHistory:
    all = {}

    def __init__(self, user_id, book_id, borrowed_date, return_date=None, id=None):
        self.id = id
        self.user_id = user_id
        self.book_id = book_id
        self.borrowed_date = borrowed_date
        self.return_date = return_date
        
    def _repr_(self):
        return f"<BorrowingHistory {self.id}: User ID={self.user_id}, Book ID={self.book_id}, Borrowed Date='{self.borrowed_date}', Return Date='{self.return_date}'>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS borrowing_history (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                book_id INTEGER,
                borrowed_date TEXT,
                return_date TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS borrowing_history"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO borrowing_history (user_id, book_id, borrowed_date, return_date) VALUES (?, ?, ?, ?)"
        CURSOR.execute(sql, (self.user_id, self.book_id, self.borrowed_date, self.return_date))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = "UPDATE borrowing_history SET user_id = ?, book_id = ?, borrowed_date = ?, return_date = ? WHERE id = ?"
        CURSOR.execute(sql, (self.user_id, self.book_id, self.borrowed_date, self.return_date, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM borrowing_history WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, user_id, book_id, borrowed_date, return_date=None):
        history = cls(user_id, book_id, borrowed_date, return_date)
        history.save()
        return history

    @classmethod
    def instance_from_db(cls, row):
        history = cls.all.get(row[0])
        if history:
            history.user_id = row[1]
            history.book_id = row[2]
            history.borrowed_date = row[3]
            history.return_date = row[4]
        else:
            history = cls(row[1], row[2], row[3], row[4], row[0])
            cls.all[history.id] = history
        return history

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM borrowing_history"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_user(cls, user_id):
        sql = "SELECT * FROM borrowing_history WHERE user_id = ?"
        rows = CURSOR.execute(sql, (user_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_book(cls, book_id):
        sql = "SELECT * FROM borrowing_history WHERE book_id = ?"
        rows = CURSOR.execute(sql, (book_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]