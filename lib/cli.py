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
            print("\nInvalid choice")

def menu():
    print("\nWelcome to BLOGGER!")
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
        if choice == "0":
            exit_program()
        elif choice == "1":
            main()
        elif choice == "2":
            add_author()
            create_menu()
        elif choice == "3":
            write_post()
            create_menu()
        else:
            print("Invalid choice")

def create_menu_options():
    print("\n-Now in Create Menu-")
    print("Please select an option:")
    print("0. Exit Program")
    print("1. Return to Main Menu")
    print("2. Add a New Author")
    print("3. Write a Post")
    


#? View Menu
def view_menu():
    while True:
        view_menu_options()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            main()
        elif choice == "2":
            view_authors()
        elif choice == "3":
            find_author_by_id()
        elif choice == "4":
            find_author_by_name()
        elif choice == "5":
            view_authors_posts()
        elif choice == "6":
            view_all_posts()
        elif choice == "7":
            view_posts_by_category()
        elif choice == "8":
            find_number_of_posts_by_author()
        else:
            print("Invalid choice")
        view_menu()

def view_menu_options():
    print("\n-Now in Viewing Menu-")
    print("Please select an option:")
    print("0. Exit Program")
    print("1. Return to Main Menu")
    print("2. View all authors")
    print("3. Find author by id")
    print("4. Find author by name")
    print("5. View all post by specific author")
    print("6. View all posts")
    print("7. View all posts by category")
    print("8. Find number of posts by author")
    


#? Edit Menu
def edit_menu():
    while True:
        edit_menu_options()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            main()
        elif choice == "2":
            edit_author()     
        elif choice == "3":
            edit_post()
        else :
            print("Invalid choice")

def edit_menu_options():
    print("\n-Now in Edit Menu-")
    print("Please select an option:")
    print("0. Exit Program")
    print("1. Return to Main Menu")
    print("2. Edit an author")
    print("3. Edit a post")
    


#? Delete Menu
def delete_menu():
    while True:
        delete_menu_options()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            main()    
        elif choice == "2":
            delete_author()
        elif choice == "3":
            delete_post()
        else :
            print("Invalid choice")


def delete_menu_options():
    print("\n-Now in Delete Menu-")
    print("Please select an option:")
    print("0. Exit Program")
    print("1. Return to Main Menu")
    print("2. Delete an author")
    print("3. Delete a post")
    



if __name__ == "__main__":
    main()
