from models.__init__ import CURSOR, CONN
from models.post import Post

class Author:
    all = {}

    def __init__ (self, name, favorite_category, id=None):
        self.name = name
        self.favorite_category = favorite_category
        self.id = id

    def __repr__(self):
        return f'<Author name={self.name} favorite_category={self.favorite_category}>'
    

    @property
    def name(self):
        return self._name
    
    #name must be str and between 1 and 15 characters inclusive
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 0 < len(new_name) <= 15:
            self._name = new_name

    @property
    def favorite_category(self):
        return self._favorite_category
    
    @favorite_category.setter
    def favorite_category(self, new_category):
        if new_category in Post.categories:
            self._favorite_category = new_category
        else:
            raise ValueError("Category must be a valid category")

    #? Creates author table if it doesn't already exist
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Author instances """
        sql = """
            CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT,
            favorite_category TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    #? Deletes the author table 
    @classmethod
    def drop_table(cls):
        """ Drop the table to persist the attributes of Post instances """
        sql = "DROP TABLE IF EXISTS authors"

        CURSOR.execute(sql)
        CONN.commit()
    
    #? Saves  an author to the database
    def save(self):
        """ Insert a new row with the the name of the author object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO authors (name, favorite_category)
                VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.favorite_category))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    #? Creates and saves author to the database
    @classmethod
    def create(cls, name, favorite_category):
        """ Initialize a new Author instance and save the object to the database """
        author = cls(name, favorite_category)
        author.save()
        return author
    
    #? Updates author and saves to database
    def update(self):
        """Update the table row corresponding to the current Author instance."""
        sql = """
            UPDATE authors
            SET name = ?, favorite_category = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.favorite_category, self.id))
        CONN.commit()

    #? Deltes author from database
    def delete(self):
        """Delete the table row corresponding to the current Author instance,
        delete the author entry, and reassign id attribute"""

        sql = """
            DELETE FROM authors
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None
    

    #? Checks to see if an author exists in database
    @classmethod
    def instance_from_db(cls, row):
        """Return an Author object having the attribute values from the table row."""

        #Check the dictionary for an existing instance using the row's primary key
        author = cls.all.get(row[0])
        if author:
            # ensure attributes match row values in case local instance was modified
            author.name = row[1]
            author.favorite_category = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            author = cls(row[1], row[2])
            author.id = row[0]
            cls.all[author.id] = author
        return author

    #? Returns list of all authors from database
    @classmethod 
    def get_all(cls):
        """Return a list containing an Author object per row in the table"""
        sql = """
            SELECT *
            FROM authors
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    #? Finds an author from database by their id
    @classmethod 
    def find_by_id(cls, id):
        """Return a Author object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM authors
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    #? Finds author from database by their name
    @classmethod
    def find_by_name(cls, name):
        """Return an Author object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM authors
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    #? Finds all posts of author instance from database
    def find_all_posts(self):
        """Return a list of Post objects associated with this Author"""
        try:
            return [post for post in Post.get_all() if post.author_id == self.id]
        except: Exception("No posts found by author")