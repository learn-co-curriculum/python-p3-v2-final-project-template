# lib/cli.py

from helpers import (
    exit_program,
    #helper_1,
    list_bands,
    find_band_by_name,
    find_band_by_id,
    create_band,
    update_band,
    delete_band,
    list_concerts,
    find_concert_by_name,
    find_concert_by_id,
    create_concert,
    update_concert,
    delete_concert,
)
from helpers import app
# import typer

@app.command()
def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_bands()
        elif choice == "2":
            find_band_by_name()
        elif choice == "3":
            find_band_by_id()
        elif choice == "4":
            create_band()
        elif choice == "5":
            update_band()
        elif choice == "6":
            delete_band()
        elif choice == "7":
            list_concerts()
        elif choice == "8":
            find_concert_by_name()
        elif choice == "9":
            find_concert_by_id()
        elif choice = "10":
            create_concert()
        elif choice = "11":
            update_concert()
        elif choice = "12":
            delete_concert()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all bands")
    print("2. Find a band by name")
    print("3. Find a band by id")
    print("4. Create a band")
    print("5. Update a band")
    print("6. Delete a band")
    print("7. List all concerts")    
    print("8. Find a concert by name")
    print("9. Find a concert by id")
    print("10. Create a concert")
    print("11. Update a concert")
    print("12. Delete a concert")




if __name__ == "__main__":
    # typer.run(main)
    app()
