from models.__init__ import CURSOR, CONN

class Post():
    all = {}
    categories = ['sports', 'news', 'pop', 'nature', 'weather', 'cars', 'movies']


    def __init__(self, title, content, category, author_id, id = None):
        self.id = id
        self.title = title
        self.content = content
        self.category = category
        self.author_id = author_id

    def __repr__(self):
        return f"<Post title={self.title}, content={self.content}, category={self.category}, id={self.id}, author_id={self.author_id}>"
    
    @property
    def title(self):
        return  self._title
    
    #? only accepts type str and 1 to 20 characters
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and 0 < len(new_title) <= 20:
            self._title = new_title

    @property 
    def content(self):
        return self._content
    
    #? only accepts type str and at least 1 charachter
    @content.setter
    def content(self, new_content):
        if isinstance(new_content, str) and len(new_content) > 0:
            self._content = new_content

    @property
    def category(self):
        return self._category
    
    #? only accepts if category is in categories
    @category.setter
    def category(self, new_category):
        if new_category in Post.categories:
            self._category = new_category

    
    #? Creates posts table if it doesn't already exist
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Post instances """
        sql = """
            CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT,
            category TEXT,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    #? Deletes the posts table 
    @classmethod
    def drop_table(cls):
        """ Drop the table to persist the attributes of Post instances """
        sql = "DROP TABLE IF EXISTS posts"

        CURSOR.execute(sql)
        CONN.commit()

    #? Save the  post to the database
    def save(self):
        """ Insert a new row with the title, content, category and author_id values of the current Post object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO posts (title, content, category, author_id)
                VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.content, self.category, self.author_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    #? Updates the post in the database based on the instance's attributes
    def update(self):
        """Update the table row corresponding to the current Post instance."""
        sql = """
            UPDATE posts
            SET title = ?, content = ?, category = ?, author_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.content,
                             self.category, self.author_id, self.id))
        CONN.commit()

    #? Deletes the post from the database and updates the local dictionary
    def delete(self):
        """Delete the table row corresponding to the current Post instance,
        delete the dictionary entry, and reassign id attribute"""
        sql = """
            DELETE FROM posts
            WHERE id = ?
        """
    
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
    
        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        #Set the id to none 
        self.id = None

    #? Creates a new post instance to be put in database and dictionary
    @classmethod
    def create(cls, title, content, category, author_id):
        """Create a new Post instance and save it to the database."""
        post = cls(title, content, category, author_id)
        post.save()
        return post
    
    #? Checks if there is an instance of the post in the database
    @classmethod
    def instance_from_db(cls, row):
        """Return a Post object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        post = cls.all.get(row[0])
        if post:
            # ensure attributes match row values in case local instance was modified
            post.name = row[1]
            post.job_title = row[2]
            post.department_id = row[3]
            post.author_id = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            post = cls(row[1], row[2], row[3], row[4])
            post.id = row[0]
            cls.all[post.id] = post
        return post
    
    #? Retrieves all posts from the database
    @classmethod
    def get_all(cls):
        """Return a list containing one Post object per table row"""
        sql = """
            SELECT *
            FROM posts
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    #? Find the post instance by id from the database using the instance-from-db method
    @classmethod
    def find_by_id(cls, id):
        """Return Post object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM posts
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    #? Find the post instance by title from the database using the instance-from-db method
    @classmethod
    def find_by_title(cls, title):
        """Return Post object corresponding to first table row matching specified title"""
        sql = """
            SELECT *
            FROM posts
            WHERE title is ?
        """

        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    #? Returns list of posts by a specific category
    @classmethod
    def find_by_category(cls, category):
        """Return list of Post objects corresponding to table rows matching specified category"""
        return [post for post in cls.get_all() if post.category == category]
       
