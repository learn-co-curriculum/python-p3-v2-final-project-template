# category.py
from __init__ import CONN  

class Category:
    """Represents a category for quiz questions."""

    def __init__(self, name, category_id=None):
        """Initialize a new Category instance."""
        self.id = category_id
        self.name = name

    @staticmethod
    def create_table():
        """Create the category table in the database if it does not exist."""
        cursor = CONN.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        ''')
        CONN.commit()

    def save(self):
        """Save the current instance to the database."""
        cursor = CONN.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO categories (name) VALUES (?)', (self.name,))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE categories SET name = ? WHERE id = ?', (self.name, self.id))
        CONN.commit()

    @staticmethod
    def get_all():
        """Retrieve all categories from the database."""
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM categories')
        return cursor.fetchall()

    @staticmethod
    def find_by_id(category_id):
        """Find a category by its ID."""
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM categories WHERE id = ?', (category_id,))
        return cursor.fetchone()

    @staticmethod
    def find_by_name(name):
        """Find a category by its name."""
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM categories WHERE name = ?', (name,))
        return cursor.fetchone()

    @staticmethod
    def delete(category_id):
        """Delete a category by its ID."""
        cursor = CONN.cursor()
        cursor.execute('DELETE FROM categories WHERE id = ?', (category_id,))
        CONN.commit()
        

# Example usage
if __name__ == "__main__":
    # Create the categories table
    Category.create_table()

    # Create a new category
    new_category = Category('Science')
    new_category.save()  # Save the new category to the database

    # Get all categories
    all_categories = Category.get_all()
    print(all_categories)

    # Find a category by ID
    category = Category.find_by_id(1)
    print(category)

    # Find a category by name
    category = Category.find_by_name('Science')
    print(category)

    # Update a category
    category_to_update = Category('Mathematics', category_id=1)
    category_to_update.save()

    # Delete a category
    Category.delete(1)