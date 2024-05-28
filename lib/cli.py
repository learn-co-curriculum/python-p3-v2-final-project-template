# lib/cli.py

from helpers import (
    exit_program,
    add_author,
    write_post,
    edit_author,
    edit_post,
    view_authors,
    find_author_by_id,
    find_author_by_name,
    view_authors_posts,
    view_all_posts,
    view_posts_by_category,
    find_number_of_posts_by_author,
    delete_post,
    delete_author
)

#? Main Menu
def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_menu()
        elif choice == "2":
            view_menu()
        elif choice == "3":
            edit_menu()
        elif choice == "4":
            delete_menu()
        else:
            print("Invalid choice")

def menu():
    print("Welcome to BLOGGER!")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create Author or Post")
    print("2. View Authors and Posts")
    print("3. Edit Author or Post")
    print("4. Delete Author or Post")


#? Create Menu
def create_menu():
    while True:
        create_menu_options()
        choice = input("> ")
        if choice == "1":
            add_author()
            create_menu()
        elif choice == "2":
            write_post()
            create_menu()
        elif choice == "3":
            main()
        else:
            print("Invalid choice")

def create_menu_options():
    print("Please select an option:")
    print("1. Add an author")
    print("2. Write a post")
    print("3. Return to Main Menu")


#? View Menu
def view_menu():
    while True:
        view_menu_options()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            view_authors()
        elif choice == "2":
            find_author_by_id()
        elif choice == "3":
            find_author_by_name()
        elif choice == "4":
            view_authors_posts()
        elif choice == "5":
            view_all_posts()
        elif choice == "6":
            view_posts_by_category()
        elif choice == "7":
            find_number_of_posts_by_author()
        elif choice == "8":
            main()
        else:
            print("Invalid choice")
        view_menu()

def view_menu_options():
    print("Please select an option:")
    print("0. Exit Program")
    print("1. View all authors")
    print("2. Find author by id")
    print("3. Find author by name")
    print("4. View all post by specific author")
    print("5. View all posts")
    print("6. View all posts by category")
    print("7. Find number of posts by author")
    print("8. Return to main menu")


#? Edit Menu
def edit_menu():
    while True:
        edit_menu_options()
        choice = input("> ")
        if choice == "1":
            edit_author()     
        elif choice == "2":
            edit_post()
            
        elif choice == "3":
            main()

def edit_menu_options():
    print("Please select an option:")
    print("1. Edit an author")
    print("2. Edit a post")
    print("3. Return to Menu")


#? Delete Menu
def delete_menu():
    while True:
        delete_menu_options()
        choice = input("> ")
        if choice == "1":
            delete_author()
        elif choice == "2":
            delete_post()
        elif choice == "3":
            main()


def delete_menu_options():
    print("Please select an option:")
    print("1. Delete an author")
    print("2. Delete a post")
    print("3. Return to Menu")



if __name__ == "__main__":
    main()
