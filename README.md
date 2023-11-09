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
    try:
        Contact.create(name)
    except ValueError:
        print("Please type a valid name in order to create a person")
```
Allows the user to create a new contact by providing a name.

```py
def create_an_address():
    show_all_contacts()
    email = input(f"type email address: ")
    id = input(f"Type id number: ")

    try:
        id = int(id)
        if not isinstance(email,str):
            raise ValueError("Email must be a string.")
        
        Address.create(email,id)
        print("Address created successfully")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
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
def address_by_id():
    try:
        id= int(input("Enter the ID for the contact whose email you are looking for: "))
        emails = Address.get_email(id)
        if emails:
            print(f"Contact found: {emails}")
            for email in emails:
                print(email)
        else: 
            print("Contact not found.")
    except ValueError:
        print("Invalid input. Please enter a valid contact ID.")
```
Searches for Email address by ID. 
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
            find_by_id()
        elif c == 7:
            find_by_name()
        elif c == 8:
            address_by_id()
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
    print("6. find a contact by id")
    print("7. find a contact by name")
    print("8. find email by contact id")

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
def create(email:str, person_id:int):
        sql = "INSERT INTO addresses (email, person_id) VALUES (?, ?)"
        c = CURSOR.execute(sql, (email, person_id))
        CONN.commit()
        return c.lastrowid

```
The SQL statement "INSERT INTO contacts (name) VALUES (?)" is used to create an SQL command to insert a new record into the "contacts" table. It specifies that you want to insert a value into the "name" column.

The CURSOR.execute method is used to execute the SQL statement. The ? in the SQL statement is a placeholder for a parameterized query, and the actual value to be inserted is passed as a tuple (name,). This helps prevent SQL injection and ensures that the value is properly sanitized.

After executing the SQL statement, the CONN.commit() method is called to commit the changes to the database. This is necessary to persist the changes you made by inserting a new record.

The function returns c.lastrowid, which is the last inserted row's ID. This can be useful if you want to retrieve the ID of the newly inserted record.
```py
def read_by_person_id(person_id:int):
        sql = "select (id, email, person_id) from addresses where person_id = ?"
        return CURSOR.execute(sql, (person_id,))
```
the function is a database retrieval operation that fetches data from the "addresses" table based on a given person ID. The returned data would likely include the ID, email, and person ID for the matching rows in the database.
```py
@classmethod
    def get_email (cls, person_id):
        sql = 'SELECT email FROM addresses where person_id= ?'
        CURSOR.execute(sql, (person_id,))
        results= CURSOR.fetchall()
        if results:
            emails = [result[0] for result in results]
            return emails
            # return Address.from_db(result)
        else:
            return None
```
This class method is designed to be called on the class itself (YourClass.get_email(person_id)) and it retrieves email addresses from the 'addresses' table in the database based on the provided 'person_id'.

```py
@classmethod
    def all(cls):
        sql = 'SELECT * FROM addresses'
        list_of_tuples = CURSOR.execute(sql).fetchall()
        return [Address.from_db ( row ) for row in list_of_tuples]
```
This class method is used to retrieve all addresses from a database and return them as a list of Address objects. The Address.from_db(row) method is assumed to be responsible for creating an Address object from a database row.
```py
@classmethod
    def from_db(cls, row_tuple):
        address_instance = Address(row_tuple[1], row_tuple[2])
        address_instance.id = row_tuple[0]
        return address_instance
```
This method is a way to instantiate an Address object from a database row represented as a tuple. It extracts relevant information from the tuple and sets the attributes of the Address instance accordingly.

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
  @classmethod
    def get_id (cls, id):
        sql = 'SELECT * FROM contacts WHERE id = ?'
        CURSOR.execute(sql, (id,))
        result = CURSOR.fetchone()
        if result:
            return Contact.from_db(result)
        else:
            return None
 ```
 This method is used to retrieve a contact from a database by its ID. If the contact exists, it returns a Contact object; otherwise, it returns None. The actual implementation of from_db in the Contact class would be needed to fully understand the behavior.

 ```py
 @classmethod
    def get_name (cls, name):
        sql = 'SELECT * FROM contacts where name= ?'
        CURSOR.execute(sql, (name,))
        result= CURSOR.fetchone()
        if result:
            return Contact.from_db(result)
        else:
            return None
 ```
This class method is designed to retrieve contact information from a database based on a given name and return it as a Contact object if found, or None if not found.

```py
 @classmethod 
    def all(cls):
        sql = 'SELECT * FROM contacts'
        list_of_tuples = CURSOR.execute(sql).fetchall()
        return [Contact.from_db ( row ) for row in list_of_tuples]
 ```
 This class method provides a way to retrieve all contacts from the database as a list of Contact objects. 

```py
@classmethod
    def from_db( cls, row_tuple ):
        contact_instance = Contact( row_tuple[1])
        contact_instance.id = row_tuple[0]
        return contact_instance
    
 ```
This method is useful when you retrieve data from a database and want to create Contact instances based on the retrieved rows. Instead of manually creating instances and setting attributes.


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

```py
 def addresses(self):
        from address import Address
        sql= """"
            SELECT * FROM addresses
            WHERE person_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Address.instance_from_db(row) for row in rows
        ]
```
This code fetches addresses associated with a person from a database by executing a SQL query, and then it creates a list of Address instances based on the query results. I

---


## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
