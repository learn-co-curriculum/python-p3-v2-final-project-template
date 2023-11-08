#lib/cli.py
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
    find_brand_by_driver_name
)

def main():
    while True:
        menu()
        choice = input("> ")
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
def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. LIST ALL car BRANDS")
    print("2. CREATE a New Car BRAND")
    print("3. DELETE an Existing Car BRAND")
    print("4. FIND Car BRAND by Name")
    print("5. LIST all BRANDS of a Specific Country")
    print("6. LIST all Existing DRIVERS")
    print("7. CREATE a New DRIVER")
    print("8. DELETE an existing DRIVER")
    print("9. FIND an existing DRIVER by name")
    print("10.List all DRIVERS of a specific BRAND #")
    print("11. Find BRAND by DRIVER name")


if __name__ == "__main__":
    main()