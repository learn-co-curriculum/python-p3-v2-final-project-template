# lib/cli.py

from helpers import (
    exit_program,
    list_reviewers,
    find_reviewer_by_id,
    create_reviewer,
    update_reviewers,
    delete_reviewer,
    list_posts,
    find_post_by_id,
    create_post,
    update_post,
    delete_post
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_reviewers()
        elif choice == "2":
            find_reviewer_by_id()
        elif choice == "3":
            create_reviewer()
        elif choice == "4":
            update_reviewers()
        elif choice == "5":
            delete_reviewer()
        elif choice == "6":
            list_posts()
        elif choice == "7":
            find_post_by_id()
        elif choice == "8":
            create_post()
        elif choice == "9":
            update_post()
        elif choice == "10":
            delete_post()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all reviewers")
    print("2. Find reviewer by id")
    print("3: Create reviewer")
    print("4: Update reviewer")
    print("5: Delete reviewer")
    print("6. List all posts")
    print("7. Find post by id")
    print("8: Create post")
    print("9: Update post")
    print("10: Delete post")

if __name__ == "__main__":
    main()
