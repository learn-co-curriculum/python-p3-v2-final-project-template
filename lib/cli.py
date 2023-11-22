from models.brand import Brand
from helpers import (
    exit_program,
    list_brands,
    create_brand,
    delete_brand,
    find_brand_by_name,
    list_brands_by_country,
    create_driver,
    list_drivers,
    delete_driver,
    find_driver_by_name,
    list_drivers_by_brand,
    find_brand_by_driver_name,
    start_game,
)

def main():

    
    print("----------------------------------")
    print("                                  ")
    print("    🏁 FLATIRON ARCADE RACER 🏁    ")
    print("                                  ")
    print("      🚕    🏎️💨    🚗    🚚        ")
    print("----------------------------------")


    while True:
        menu()
        choice = input("Select an option (0-11): ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_brands()
        elif choice == "2":
            create_brand()
        elif choice == "3":
            delete_brand()
        elif choice == "4":
            find_brand_by_name()
        elif choice == "5":
            list_brands_by_country()
        elif choice == "6":
            list_drivers()
        elif choice == "7":
            create_driver()
        elif choice == "8":
            delete_driver()
        elif choice == "9":
            find_driver_by_name()
        elif choice == "10":
            list_drivers_by_brand()
        elif choice == "11":
            find_brand_by_driver_name()
        elif choice == "11":
            start_game()
        elif choice == "12":            
        else:
            print("Invalid choice. Please select a valid option.")

def menu():
    print("\nGET OUT THERE AND START RACING")
    print("------------------------------------------")
    print("0.  🚫Quit Game")
    print("------------------------------------------")
    print("1.  🏁 List all Cars")
    print("------------------------------------------")
    print("2.  🚀 Create a new Car")
    print("------------------------------------------")
    print("3.  🗑️ Delete an existing car brand")
    print("------------------------------------------")
    print("4.  🔍 Find a car brand by name")
    print("------------------------------------------")
    print("5.  🌍 List all brands of a specific country")
    print("------------------------------------------")
    print("6.  🚗 List all existing drivers")
    print("------------------------------------------")
    print("7.  🏎️ Create a new driver")
    print("------------------------------------------")
    print("8.  🗑️ Delete an existing driver")
    print("------------------------------------------")
    print("9.  🔍 Find an existing driver by name")
    print("------------------------------------------")
    print("10. 🏁List all drivers of a specific brand")
    print("------------------------------------------")
    print("------------------------------------------")
    print("------------------------------------------")
    print("11. \033[1m\033[33m--------------- START GAME ---------------\033[0m")
    print("------------------------------------------")
    print("------------------------------------------")


def start_game():
    print("Welcome to the START GAME page.")
    while True:
        start_game_menu()
        choice = input("Choose from the menu below:")

        if choice == "0":
            return  # Return to the main menu
        elif choice == "1":
            list_drivers()
        else:
            print("Invalid choice. Please select a valid option.")


def start_game_menu():
    print("START GAME MENU")
    print("------------------------------------------")
    print("0.  Return to main menu")
    print("------------------------------------------")
    print("1.  PICK YOUR DRIVER")
    print("------------------------------------------")

 

if __name__ == "__main__":
    main()

