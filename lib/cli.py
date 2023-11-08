from models.brand import Brand
from helpers import (
    exit_program,
    helper_1,
    list_brands,
    create_brand,
    delete_brand,
    find_brand_by_name,
    list_brands_by_country,
    create_driver,
    list_drivers,
    delete_driver,
    find_driver_by_name,
    list_drivers_by_brand
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
        choice = input("Select an option (0-10): ")
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
    print("")

if __name__ == "__main__":
    main()
