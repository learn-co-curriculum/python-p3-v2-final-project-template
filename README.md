# Phase 3 Arcade Membership Management CLI Application

## Learning Goals

- Discuss the basic directory structure of a CLI.
- Outline the first steps in building a CLI.

---

## Introduction

You now have a basic idea of what constitutes a CLI. Fork and clone this lesson for a project template for your CLI.

Take a look at the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── arcade.py
    │   ├── locale.py
    │   └── member.py
    ├── cli.py
    ├── debug.py
    └── helpers.py


## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---

## Generating Your CLI

A CLI is, simply put, an interactive script that prompts the user and performs operations based on user input.

The project template has a sample CLI in `lib/cli.py` that looks like this:

```py
# lib/cli.py

from helpers import menu, exit_program
from models.arcade import Arcade
from models.locale import Locale
from models.member import Member


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_arcade()
        elif choice == "2":
            delete_arcade()
        elif choice == "3":
            display_all_arcades()
        elif choice == "4":
            view_members_of_arcade()
        elif choice == "5":
            find_arcade_by_tag()
        else:
            print("Invalid choice")


def create_arcade():
    name = input("Enter member name: ")
    tag = input("Enter membership tag: ")
    location = int(input("Enter location number (1, 2, or 3): "))
    arcade = Arcade(name, tag, location)
    print("Arcade created successfully!")


def delete_arcade():
    # Add logic to delete an arcade
    pass


def display_all_arcades():
    print("List of all Arcades:")
    for arcade in Arcade.all:
        print(arcade)
    print()


def view_members_of_arcade():
    # Add logic to view members of an arcade
    pass


def find_arcade_by_tag():
    tag = input("Enter membership tag: ")
    found_arcade = [arcade for arcade in Arcade.all if arcade.tag == tag]
    if found_arcade:
        print("Arcade found:")
        print(found_arcade)
    else:
        print("No arcade found with that tag.")


if __name__ == "__main__":
    main()
The helper functions are located in lib/helpers.py:

py
Copy code
# lib/helpers.py

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create Arcade")
    print("2. Delete Arcade")
    print("3. Display All Arcades")
    print("4. View Members of an Arcade")
    print("5. Find Arcade by Tag")


def exit_program():
    print("Goodbye!")
    exit()
In this updated example, we've incorporated functions to interact with the Arcade model from your code. The CLI prompts the user to perform various operations related to creating, deleting, displaying, and finding arcades. You can similarly add functions to interact with the Locale and Member models as needed.

You can run the template CLI with `python lib/cli.py`, or include the shebang
and make it executable with `chmod +x`. The template CLI will ask for input, do
some work, and accomplish some sort of task.

Past that, CLIs can be whatever you'd like, as long as you follow the project
requirements.

Of course, you will update `lib/cli.py` with prompts that are appropriate for
your application, and you will update `lib/helpers.py` to replace `helper_1()`
with a useful function based on the specific problem domain you decide to
implement, along with adding other helper functions to the module.

In the `lib/models` folder, you should rename `model_1.py` with the name of a
data model class from your specific problem domain, and add other classes to the
folder as needed. The file `lib/models/__init__.py` has been initialized to
create the necessary database constants. You need to add import statements to
the various data model classes in order to use the database constants.

You are also welcome to implement a different module and directory structure.
However, your project should be well organized, modular, and follow the design
principal of separation of concerns, which means you should separate code
related to:

- User interface
- Data persistence
- Problem domain rules and logic

---

## Updating README.md

`README.md` is a Markdown file that should describe your project. You will
replace the contents of this `README.md` file with a description of **your**
actual project.

Markdown is not a language that we cover in Flatiron's Software Engineering
curriculum, but it's not a particularly difficult language to learn (if you've
ever left a comment on Reddit, you might already know the basics). Refer to the
cheat sheet in this assignments's resources for a basic guide to Markdown.

### What Goes into a README?

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

---

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you off
to a good start with your Phase 3 Project.

Happy coding!

