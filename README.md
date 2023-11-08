# Phase 3 Project

## 2 models:

- Contact class
    - hold the persons name and id
- Address class
    - holds the person's emails
    - so one person can have multiple emails

---

## Introduction



Take a look at the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── address.py
    │   └── contact.py
    ├── cli.py
    ├── create_db.py
    ├── debug.py
    └── helpers.py
```

`CONTRIBUTING.md` and `LICENSE.md` part of Flatiron's curriculum. 

---

## Generating Your Environment

'Pipfile" already installeld. 
Run the commands: 

```console
pipenv install
pipenv shell
```

---

## Generating Your CLI


This project template has a CLI in `lib/cli.py` that looks like this:

```py
# lib/cli.py

from models.contact import Contact
from models.address import Address
```
The script imports the Contact and Address classes from their respective modules.

```py
def create_a_person():
    name = input("type name to create:")
    Contact.create(name)
```
Allows the user to create a new contact by providing a name.

```py
def create_an_address():
    show_all_contacts()
    email = input(f"type email address: ")
    id = input(f"type id: ")
    Address.create(email, int(id))
```
Lets the user create a new address associated with an existing contact.

```py
def show_all_contacts():
    contacts = Contact.all()
    print("===all contacts===")
    for c in contacts:
        print(c)
    print("==============")
    return contacts
```
Displays a list of all contacts in the address book.
```py
def show_all_addresses():
    addresses = Address.read_all()
    print("===all addresses===")
    for c in addresses:
        print(c)
    print("==============")
    return addresses
```
Displays a list of all addresses in the address book.
```py
def find_by_id():
    try:
        id = int(input("Enter the contact ID: "))
        contact = Contact.get_id(id)
        if contact:
            print(f"Contact found: \n{contact}")
        else:
            print("Contact not found.")
    except ValueError:
        print("Invalid input. Please enter a valid contact ID.")
```
Searches for a contact by its ID.
```py
def exit_program():
    print("Goodbye!")
    exit()
```
Exits the program    
```py
def delete_contact():
    show_all_contacts()
    id = input("type the id to delete: ")
    Contact.delete(int(id))
```
Deletes a contact by its ID.
```py
def show_contact_detail():
    show_all_contacts()
    id = input("type the id to see the detail: ")
    Contact.show_detail(int(id))
```
Displays detailed information about a contact by its ID.
```py
def main():
    while True:
        menu()
        choice = input("> ")
        c = int(choice)
        if c == 0:
            exit_program()
        elif c == 1:
            create_a_person()
        elif c == 2:
            create_an_address()
        elif c == 3:
            show_all_contacts()
        elif c == 4:
            show_all_addresses()
        elif c == 5:
            delete_contact()
        elif c == 6:
            show_contact_detail()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. create a person")
    print("2. create an email address")
    print("3. show all contact")
    print("4. show all address")
    print("5. delete a contact")
    print("6. show a contact details")

```
This function serves as the main entry point of the application and runs an interactive loop.
Inside the loop, it calls the menu() function to display the available menu options.
The user is prompted to select an option by entering a number.
Based on the user's choice, the corresponding function is called to perform the desired operation.

---

## Address.py
```py
    def __init__(self, email:str, person_id:int):
        self.email = email
        self.person_id = person_id
```
The instance of the Address class is initialized with the email and person_id attributes.

```py
 def __repr__(self):
        return f"Address(email={self.email}, person_id={self.person_id})" 
```
In the example above, the __repr__ method is defined to return a string that represents the Address object with its email and person_id attributes. When you use repr(address), it returns a string that helps you understand the object's state. This can be especially useful for debugging and logging.
```py
 @property
    def id(self):
        return self._id
```
The code you've provided defines a property named id using the @property decorator. This allows you to access the id attribute of an object as if it were an instance variable, even though it's actually derived from the private attribute _id.
```py
def __create_table__():
        sql = """create table addresses (
            id INTEGER NOT NULL, 
            email VARCHAR(30) NOT NULL, 
            person_id INTEGER NOT NULL, 
            PRIMARY KEY (id),
            FOREIGN KEY(person_id) REFERENCES contacts (id)
        );
        """
        CURSOR.execute(sql)
```
CREATE TABLE addresses specifies that you're creating a new table named "addresses."
The table has three columns: id, email, and person_id, each with a specified data type (INTEGER and VARCHAR).
NOT NULL is used to indicate that these columns cannot have null values.
PRIMARY KEY (id) designates the id column as the primary key for the table, ensuring that it contains unique values and is not null.
FOREIGN KEY (person_id) REFERENCES contacts (id) defines a foreign key constraint that links the person_id column to the id column in a table named "contacts." This enforces referential integrity, ensuring that the values in the person_id column correspond to existing records in the "contacts" table.
```py
def create(name: str):
        sql = "INSERT INTO contacts (name) VALUES (?)"
        c = CURSOR.execute(sql, (name,))
        CONN.commit()
        return c.lastrowid

```
The SQL statement "INSERT INTO contacts (name) VALUES (?)" is used to create an SQL command to insert a new record into the "contacts" table. It specifies that you want to insert a value into the "name" column.

The CURSOR.execute method is used to execute the SQL statement. The ? in the SQL statement is a placeholder for a parameterized query, and the actual value to be inserted is passed as a tuple (name,). This helps prevent SQL injection and ensures that the value is properly sanitized.

After executing the SQL statement, the CONN.commit() method is called to commit the changes to the database. This is necessary to persist the changes you made by inserting a new record.

The function returns c.lastrowid, which is the last inserted row's ID. This can be useful if you want to retrieve the ID of the newly inserted record.
```py
def read_all():
        sql = "select id, name from contacts"
        rows = CURSOR.execute(sql)
        ret = []
        for (id, name) in rows:
            person = Contact(name)
            person._id = id
            ret.append(person)
            
        return ret
```
The SQL statement "select id, name from contacts" is used to retrieve the id and name columns from the "contacts" table.

CURSOR.execute(sql) executes the SQL statement, and the result is stored in the rows variable.

An empty list ret is created to store the Contact objects that will be created from the retrieved data.

A loop iterates over each row in the rows result set, unpacking the id and name values.

For each row, a new Contact object is created with the name provided. The person._id attribute is set to the id value from the database.

The person object is then appended to the ret list.

Finally, the function returns the list ret, which contains all the Contact objects representing the records retrieved from the database.
```py
def delete(id:int):
        sql = "DELETE FROM addresses WHERE person_id=?"
        CURSOR.execute(sql, (id,))
        sql = "DELETE FROM contacts WHERE id=?"
        CURSOR.execute(sql, (id,))
        CONN.commit()
```
The first SQL statement "DELETE FROM addresses WHERE person_id=?" is used to delete records from the "addresses" table where the person_id matches the provided id. The ? is a placeholder for the parameter, and you pass the id as a tuple (id,) to the CURSOR.execute method.

The second SQL statement "DELETE FROM contacts WHERE id=?" is used to delete records from the "contacts" table where the id matches the provided id. Again, the ? is a placeholder for the parameter, and you pass the id as a tuple (id,) to the CURSOR.execute method.

After executing both SQL statements to delete records, the CONN.commit() method is called to commit the changes to the database, ensuring that the deletions take effect.

This function is designed to delete a contact and all associated addresses based on the id of the contact. It is assumed that there is a foreign key relationship between the "addresses" and "contacts" tables, with the person_id in "addresses" referencing the id in "contacts."

## Contact.py
```py
def __init__ (self, name, id=None):
        self.name = name
        self.id = id
```
The __init__ method is defined with self as the first parameter (which refers to the instance of the class being created) and name as the second parameter. Inside the __init__ method, two attributes are initialized:
_id is set to -1.
name is set to the value of the name parameter passed to the constructor.

An ID of -1 can serve as a temporary placeholder before the object is inserted into the database and receives a valid, database-generated ID.
```py   
def __repr__( self ):
        return f'id: {self.id} name: {self.name}'
```
 In your provided code, the __repr__ method returns a string that represents a "Contact" object, including its _id and name attributes.


```py
def __create_table__():
        sql = """create table contacts (
            id INTEGER NOT NULL, 
            name VARCHAR(30) NOT NULL, 
            PRIMARY KEY (id)
        );
        """
        CURSOR.execute(sql)
```
CREATE TABLE contacts specifies that you're creating a new table named "contacts."
The table has two columns:
id of type INTEGER and marked as NOT NULL. This means that the id column cannot have null values and will typically serve as the primary key for the table.
name of type VARCHAR(30) and marked as NOT NULL. This means that the name column cannot have null values and is suitable for storing character data of up to 30 characters.
PRIMARY KEY (id) designates the id column as the primary key for the table, ensuring that it contains unique values and is not null.
```py
def create(name: str):
        sql = "INSERT INTO contacts (name) VALUES (?)"
        c = CURSOR.execute(sql, (name,))
        CONN.commit()
        return c.lastrowid
```
The SQL statement "INSERT INTO contacts (name) VALUES (?)" is used to create an SQL command to insert a new record into the "contacts" table. It specifies that you want to insert a value into the "name" column.

The CURSOR.execute method is used to execute the SQL statement. The ? in the SQL statement is a placeholder for a parameterized query, and the actual value to be inserted is passed as a tuple (name,). This helps prevent SQL injection and ensures that the value is properly sanitized.

After executing the SQL statement, the CONN.commit() method is called to commit the changes to the database. This is necessary to persist the changes you made by inserting a new record.

The function returns c.lastrowid, which is the last inserted row's ID. This can be useful if you want to retrieve the ID of the newly inserted record.
```py
def read_all():
        sql = "select id, name from contacts"
        rows = CURSOR.execute(sql)
        ret = []
        for (id, name) in rows:
            person = Contact(name)
            person._id = id
            ret.append(person)
            
        return ret
```
The read_all function you've provided is designed to retrieve all records from a "contacts" table in a database and return them as a list of Contact objects. 

The SQL statement "select id, name from contacts" is used to retrieve the id and name columns from the "contacts" table.

CURSOR.execute(sql) executes the SQL statement, and the result is stored in the rows variable.

An empty list ret is created to store the Contact objects that will be created from the retrieved data.

A loop iterates over each row in the rows result set, unpacking the id and name values.

For each row, a new Contact object is created with the name provided. The _id attribute is set to the id value from the database.

The person object is then appended to the ret list.

Finally, the function returns the list ret, which contains all the Contact objects representing the records retrieved from the database.
```py
def update(name:str, id:int):
        sql = "UPDATE contacts SET name=? WHERE id=?"
        if id < 0:
            print("cannot update with unsaved data. call create first")
            return
        
        c = CURSOR.execute(sql, (name, id))
        CONN.commit()
```
The update function you've provided is intended to update the "name" of a contact with a specified id in the "contacts" table of a database.

The SQL statement "UPDATE contacts SET name=? WHERE id=?" is used to create an SQL command to update the "name" of a contact in the "contacts" table where the id matches the provided id. The ? placeholders are used for parameterized queries, and you pass the name and id as a tuple (name, id) to the CURSOR.execute method.

The function checks if the provided id is less than 0. If it's less than 0, it prints a message and returns without attempting to perform the update. This check is used to ensure that you are not trying to update data with an unsaved or invalid ID.

If the provided id is valid (greater than or equal to 0), the CURSOR.execute method is used to execute the SQL statement with the updated name.

The CONN.commit() method is called to commit the changes to the database, ensuring that the update takes effect.
```py
def delete(id:int):
        sql = "DELETE FROM addresses WHERE person_id=?"
        CURSOR.execute(sql, (id,))
        sql = "DELETE FROM contacts WHERE id=?"
        CURSOR.execute(sql, (id,))
        CONN.commit()
```
The delete function you've provided is intended to delete records from two tables, "addresses" and "contacts," based on the id parameter. Here's a breakdown of the code:

The first SQL statement "DELETE FROM addresses WHERE person_id=?" is used to delete records from the "addresses" table where the person_id matches the provided id. The ? is a placeholder for the parameter, and you pass the id as a tuple (id,) to the CURSOR.execute method.

The second SQL statement "DELETE FROM contacts WHERE id=?" is used to delete records from the "contacts" table where the id matches the provided id. Again, the ? is a placeholder for the parameter, and you pass the id as a tuple (id,) to the CURSOR.execute method.

After executing both SQL statements to delete records, the CONN.commit() method is called to commit the changes to the database, ensuring that the deletions take effect.


---


## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
