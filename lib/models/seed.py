import sqlite3

# Create a connection to an SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('company.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Drop the tables if they exist
cursor.execute('DROP TABLE IF EXISTS customer')
cursor.execute('DROP TABLE IF EXISTS drinks')
cursor.execute('DROP TABLE IF EXISTS drink_orders')

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER 
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS drinks (
    id INTEGER PRIMARY KEY,
    name TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS drink_orders (
    customer_name TEXT,
    customer_id INTEGER,
    drink_name TEXT,
    drink_id INTEGER,
    quantity INTEGER DEFAULT 1,
    PRIMARY KEY (customer_name, customer_id, drink_name, drink_id),
    FOREIGN KEY (customer_name) REFERENCES customer(name),
    FOREIGN KEY (customer_id) REFERENCES customer(id),
    FOREIGN KEY (drink_name) REFERENCES drinks(name),
    FOREIGN KEY (drink_id) REFERENCES drinks(id)
)
''')

# Function to insert data into the customer and drinks tables
def seed_db():
    # Sample user data
    customers = [
        ('Jay', 23),
        ('Victoria', 25),
        ('Kerissa', 33),
        ('Madison', 23),
        ('Johnathan', 21)
    ]
    drinks = [
        ('Cosmo',),
        ('Manhattan',),
        ('Tequila Sunrise',),
        ('Rum Runner',),
        ('Bees Knees',)
    ]

    drink_orders = [
    ('Jay', 1, 'Cosmo', 1)  # Jay ordered Cosmo
   
]

    # Insert sample customers into the database
    cursor.executemany('''
    INSERT INTO customer (name, age)
    VALUES (?, ?)
    ''', customers)

    # Insert sample drinks into the database
    cursor.executemany('''
    INSERT INTO drinks (name)
    VALUES (?)
    ''', drinks)

    cursor.executemany('''
    INSERT INTO drink_orders (customer_name, customer_id, drink_name, drink_id)
    VALUES (?, ?, ?, ?)
    ''', drink_orders)
    
    # Commit the transaction
    conn.commit()

    print(f"{len(customers)} customers added to the database.")
    print(f"{len(drinks)} drinks added to the database.")
    print(f"{len(customers)} customers, {len(drinks)} drinks, and {len(drink_orders)} drink-orders associations were added to the database.")

# Run the seed function
if __name__ == "__main__":
    seed_db()

# Close the connection
conn.close()
