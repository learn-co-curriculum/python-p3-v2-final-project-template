from classes.__init__ import CURSOR, CONN
from classes.post import Post
from classes.reviewer import Reviewer
import datetime

STATUS_VALUES = [
    0, # not done
    1, # in progress
    2  # reviewed
]

class Task:
    all = {}
    
    def __init__(self, status, created_at, updated_at, post_id, reviewer_id, id=None):
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.post_id = post_id
        self.reviewer_id = reviewer_id
        self.id = id

    def __repr__(self):
        return (
            f"<Task {self.id},"
            + f"Status {self.status},"
            + f"Created {self.created_at},"
            + f"Last Updated {self.updated_at},"
            + f"Post: {self.post_id},"
            + f"Assigned Reviewer: {self.reviewer_id}>"
        )

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status in range(3):
            self._status = status
        else:
            raise ValueError("Status must be 0, 1, or 2.")

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    @property
    def updated_at(self):
        return self._updated_at

    # @updated_at.setter
    # def updated_at(self, updated_at):
    #     if not isinstance(updated_at, datetime):
    #         raise ValueError("updated_at must be a DateTime object")
    #     elif self._updated_at <= self._created_at:
    #         raise ValueError("cannot update Task before it was created")
    #     else:
    #         self._updated_at = updated_at

    # @property
    # def post_id(self):
    #     return self._post_id

    # @post_id.setter
    # def post_id(self, post_id):
    #     if not isinstance((find_by_post_id(post_id)[0]), Post):
    #         raise ValueError("post_id is not found")
    #     else:
    #         self._post_id = post_id

    # @property
    # def reviewer_id(self):
    #     return self._reviewer_id

    # @reviewer_id.setter
    # def reviewer_id(self, reviewer_id):
    #     if not isinstance((find_by_reviewer_id(reviewer_id)[0]), Reviewer):
    #         raise ValueError("reviewer_id not found")
    #     else:
    #         self._reviewer_id = reviewer_id

    def save(self):
        try:
            with CONN:
                CURSOR.execute("""
                INSERT INTO tasks (status, created_at, updated_at, Post_id, Reviewer_id)
                VALUES (?, ?, ?, ?, ?)""",
                    (
                    self.status,
                    self.created_at,
                    self.updated_at,
                    self.post_id,
                    self.reviewer_id,
                    )
                )
        except Exception as e:
            return

    @classmethod
    def create(cls, status, created_at, updated_at, post_id, reviewer_id):
        try:
            with CONN:
               new_task = cls(status, created_at, updated_at, post_id, reviewer_id)
               new_task.save()
            return new_task
        except Exception as e:
            return e

    def update(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    UPDATE tasks SET status = ?, updated_at = ?, Post_id = ?, Reviewer_id = ?
                    WHERE id = ?
                    """,
                    (self.status, self.updated_at, self.post_id, self.reviewer_id, self.id)
                )
            # self.updated_at = updated_at.datetime().now.isoform()
        except Exception as e:
            return e

    def delete(self):
        try:
            with CONN:
                CURSOR.execute("""
                DELETE FROM tasks WHERE id = ?
                """)
        except Exception as e:
            return e

    @classmethod
    def create_table(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        status INTEGER,
                        created_at DATETIME
                        updated_at DATETIME,
                        post_id INTEGER,
                        reviewer_id INTEGER
                    );
                    """
                )
        except Exception as e:
            return e

    @classmethod
    def drop_table(cls):
      try:
          with CONN:
            CURSOR.execute("""
                DROP TABLE IF EXISTS tasks
                """) 
      except Exception as e:
          return e

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM tasks WHERE id = ?
        """
        return CURSOR.execute(sql, (id,)).fetchone() or None

    @classmethod
    def get_all(cls):
        sql = """
        SELECT * FROM tasks
        """
        return CURSOR.execute(sql).fetchall() or None

    @classmethod
    def find_by_post_id(cls, post_id):
        sql = """
        SELECT * FROM tasks WHERE post_id = ?
        """
        return CURSOR.execute(sql, (post_id,)) or None

    @classmethod
    def find_by_reviewer_id(cls, reviewer_id):
        sql = """
        SELECT * FROM tasks WHERE reviewer_id = ?
        """
        return CURSOR.execute(sql, (reviewer_id,)) or None

    @classmethod
    def find_by_status(cls, status):
        sql = """
        SELECT * FROM tasks WHERE status = ?
        """
        return CURSOR.execute(sql, (status,)) or None

    @classmethod
    def find_by_created_at(cls, created_at):
        sql = """
        SELECT * FROM tasks WHERE created_at = ?
        """
        return CURSOR.execute(sql, (created_at,)) or None

    @classmethod
    def find_by_updated_at(cls, updated_at):
        sql = """
        SELECT * FROM tasks WHERE updated_at = ?
        """
        return CURSOR.execute(sql, (updated_at,)) or None

    @classmethod
    def find_by_post_id_and_reviewer_id(cls, post_id, reviewer_id):
        sql = """
        SELECT * FROM tasks WHERE post_id = ? AND reviewer_id = ?
        """
        return CURSOR.execute(sql, (post_id, reviewer_id)) or None

    @classmethod
    def find_by_reviewer_id_and_status(cls, reviewer_id, status):
        sql = """
        SELECT * FROM tasks WHERE reviewer_id = ? AND status = ?
        """
        return CURSOR.execute(sql, (reviewer_id, status)) or None

    @classmethod
    def find_by_post_id_and_status(cls, post_id, status):
        sql = """
        SELECT * FROM tasks WHERE post_id = ? AND status = ?
        """
        return CURSOR.execute(sql, (post_id, status)) or None

    @classmethod
    def find_by_reviewer_id_and_created_at(cls, reviewer_id, created_at):
        sql = """
        SELECT * FROM tasks WHERE reviewer_id =? AND created_at =?
        """
        return CURSOR.execute(sql, (reviewer_id, created_at)) or None

    @classmethod
    def update_status(cls, id, status):
        sql = """
        UPDATE tasks SET status = ? WHERE id = ?
        """
        return CURSOR.execute(sql, (status, id))
        CONN.commit()
