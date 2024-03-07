# lib/cli.py

from helpers import (
    exit_program,
    list_bands,
    find_band_by_name,
    find_band_by_id,
    find_bands_with_genre,
    create_band,
    update_band,
    delete_band,
    list_concerts,
    find_concert_by_name,
    find_concert_by_id,
    create_concert,
    update_concert,
    delete_concert,
    list_cities,
    seed,
)
# from helpers import app
# import typer

# @app.command()
def main():
    menu()
    while True:
        print("Enter \"h\" to see the options again.")
        choice = input("> ")
        if choice == "h":
            menu()
        elif choice == "0":
            exit_program()
        elif choice == "1":
            list_bands()
        elif choice == "2":
            find_band_by_name()
        elif choice == "3":
            find_band_by_id()
        elif choice == "4":
            find_bands_with_genre()
        elif choice == "5":
            create_band()
        elif choice == "6":
            update_band()
        elif choice == "7":
            delete_band()
        elif choice == "8":
            list_concerts()
        elif choice == "9":
            find_concert_by_name()
        elif choice == "10":
            find_concert_by_id()
        elif choice == "11":
            create_concert()
        elif choice == "12":
            update_concert()
        elif choice == "13":
            delete_concert()
        elif choice == "14":
            list_cities()
        elif choice == "15":
            seed()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all bands")
    print("2. Find a band by name")
    print("3. Find a band by id")
    print("4. Find bands with genre")
    print("5. Create a band")
    print("6. Update a band")
    print("7. Delete a band")
    print("8. List all concerts")    
    print("9. Find a concert by name")
    print("10. Find a concert by id")
    print("11. Create a concert")
    print("12. Update a concert")
    print("13. Delete a concert")
    print("14. List all cities")
    print("15. Reseed tables")




if __name__ == "__main__":
    # app()
    main()