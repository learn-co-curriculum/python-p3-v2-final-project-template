# Arcade Membership Management Backend

## CLI Script (cli.py)

The `cli.py` script serves as the command-line interface for managing arcade membership. It allows users to interact with the backend system and perform various tasks such as creating new members, viewing members by location, and pulling up detailed member information.

```python
import sqlite3

conn = sqlite3.connect('arcade.db')
cursor = conn.cursor()

from helpers import (
    exit_program,
    helper_1
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            view_all_members()
        # elif choice == "2":
       
        else:
            print("Invalid choice")


def menu():
    print("Please select an option")
    print("0. Exit the program")
    print("1. View all members")
    print("2. View all arcade locations")

def exit_all():
    conn.close()
    print("Exiting the application")
    exit()

def view_all_members():
    cursor.execute("SELECT * FROM members")
    results = cursor.fetchall()

    print("All Arcade members")
    for row in results:
        print(row[1])

def helper_1():
    cursor.execute("SELECT * FROM arcades")
    results = cursor.fetchall()

    for row in results:
        print(row)

if __name__ == "__main__":
    main()
```
## Installation

To set up the project locally, follow these steps:

1. Clone the repository to your machine.
2. Install dependencies using Pipenv: `pipenv install`.
3. Activate the virtual environment: `pipenv shell`.
4. Run the CLI script: `python cli.py`.

### Functions

#### main
The `main` function is the entry point of the CLI application. It contains the main loop that displays the menu options and prompts the user for input. Based on the user's choice, it calls the corresponding functions to execute the desired actions.

#### menu
The `menu` function displays the menu options for the user to choose from. It includes options to exit the program or perform various tasks such as viewing all members or arcade locations.

#### exit_program
The `exit_program` function gracefully exits the CLI application by closing the database connection and printing a message indicating the application's termination.

#### view_all_members
The `view_all_members` function retrieves and displays all arcade members from the database. It executes an SQL query to fetch all member records and prints their details.

#### helper_1
The `helper_1` function is an example helper function included in the CLI script. It executes an SQL query to retrieve data from the `arcades` table and prints the results. This function demonstrates how additional functionality can be added to the CLI script.

### Functions

#### create_member
This function creates a new member in the arcade system. It takes parameters such as name, tag, arcade ID, and locale ID to create a new member instance and adds it to the database. Additionally, it ensures that the member's details are valid before adding them to the system.

#### get_members_by_location
This function retrieves a list of members associated with a specific arcade location. It queries the database for members belonging to the specified location and returns the results. It helps arcade staff to manage membership at different locations effectively.

#### get_member_details
This function pulls up detailed information about a specific member based on their email address. It searches the database for the member with the provided email address and returns their details. It enables arcade staff to quickly access and view specific member information as needed.

## Arcade Functions (arcade.py)

The `arcade.py` file contains functions related to managing arcade locations.

### Functions

#### Arcade Class
The `Arcade` class represents an arcade location. It provides methods for adding new locations, retrieving all locations, and saving arcade details to the database. This class helps in maintaining a record of arcade locations and managing their details effectively.

## Member Functions (member.py)

The `member.py` file contains functions related to managing arcade members.

### Functions

#### Member Class
The `Member` class represents an arcade member. It includes methods for adding new members, retrieving arcade and location details for a member, and saving member details to the database. This class facilitates the management of member information within the arcade system.

- **Init Method**: The `__init__` method initializes a new instance of the `Member` class with the specified name, tag, arcade ID, locale ID, and optional ID. It also adds the new member instance to the list of all members.

- **add_new_member Class Method**: This class method adds a new member instance to the list of all members.

- **name Property**: The `name` property allows access to the name attribute of a `Member` instance.

- **tag Property**: The `tag` property allows access to the tag attribute of a `Member` instance.

- **locale_id Property**: The `locale_id` property allows access to the locale ID attribute of a `Member` instance.

- **arcade Method**: This method returns a list of all arcade instances associated with the current member instance.

- **locale_id Method**: The `locale_id` method returns a list of locale IDs associated with the current member instance.

- **save Method**: This method saves the member details to the database by inserting a new record into the members table.

## Locale Functions (locale.py)

The `locale.py` file contains functions related to managing specific locations within an arcade.

### Functions

#### Locale Class
The `Locale` class represents a specific location within an arcade. It offers methods for adding new locations, retrieving members associated with a location, and saving location details to the database. This class assists in organizing and managing arcade locations efficiently.

## Conclusion

In conclusion, our Arcade Python project encapsulates the essence of efficient arcade management through a well-structured backend system. The CLI script, represented by `cli.py`, serves as the gateway for administrators to interact with our system, leveraging a range of functions to streamline tasks.

Throughout our project, we've meticulously crafted class instances and class properties within our models, ensuring a cohesive representation of arcade entities such as members and locations. Attributes have been thoughtfully assigned to encapsulate essential information, facilitating smooth data retrieval and manipulation.

As we wrap up, it's evident that our focus on function clarity and model integrity has laid a strong foundation for future enhancements. Each function, whether within the CLI or models, plays a vital role in empowering arcade administrators to efficiently manage memberships, locations, and member data.

Looking ahead, we're excited to continue refining and expanding our project, leveraging the power of Python to create an even more seamless experience for arcade administrators. With a keen eye on functionality and usability, we're committed to delivering a top-notch solution for arcade management needs.

For further exploration into our project's functionality, feel free to dive into the codebase and explore the intricacies of our CLI, models, and their respective functions. Your feedback and contributions are always welcome as we strive to make arcade management as enjoyable as the games themselves.
