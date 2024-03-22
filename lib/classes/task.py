from post import Post
from reviewer import Reviewer
import DateTime

class Task:
    def __init__(self, id, status, created_at, updated_at, Post_id, Reviewer_id):
        self.id = id
        self.status =[0 = 'created', 1 = 'assigned', 2= 'completed']
        self.created_at = created_at
        self.updated_at = updated_at
        self.Post_id = post_id
        self.Reviewer_id = reviewer_id

    def __repr__(self):
        return  f"<Task {self._id}," +
                f"Status {self.status}," +
                f"Created {self._created_at}," +
                f"Last Updated {self._updated_at}," +
                f"Post: {self._Post_id}," +
                f"Assigned Reviewer: {self._Reviewer_id}>"
    
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, Enum)
            self._status = status   
        else:
            raise ValueError("Status type does not exist. 

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        if not isinstance(updated_at, DateTime):
            raise ValueError("updated_at must be a DateTime object")
        elif updated_at.date() == created_at.date():
            raise ValueError("cannot update Task before it was created")
        self._updated_at = updated_at

    @property
    def Post_id(self):
        return self._Post_id    

    @post_id.setter
    def Post_id(self, post_id):
        if not isinstance(post_id, Post);
            raise ValueError("Post_id must be a Post object"
        else: = "id" and Post.id exists and Post.post_id == post
            self._post_id = post_id 
        
    @property
    def Reviewer_id(self):
        return self._Reviewer_id    

    @reviewer_id.setter
    def Reviewer_id(self, Reviewer_id):
        self._Reviewer_id = Reviewer_id

    def create_table(cls)
        sql = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status INTEGER,
            created_at DATETIME
            updated_at DATETIME,
            Post_id INTEGER,
            Reviewer_id INTEGER"""

        CURSOR.execute(sql)
        CONN.commit()
