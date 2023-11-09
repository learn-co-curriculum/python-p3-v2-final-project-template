#lib/helpers.py
from models.brand import Brand
from models.driver import Driver

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_brands():
    brands = Brand.get_all()
    if len(brands) < 1:
        print("\n No brands in database.")
    print("ID", "\t", '{0: <15}'.format("BRAND NAME"), "\t", "COUNTRY OF ORIGIN")
    for brand in brands:
        print(brand.id, "\t", '{0: <15}'.format(brand.name), "\t", brand.coo)

def create_brand():
    name = input("Enter the brand's name: ") 
    coo = input("Enter the brand's country of origin: ")
    try:
        brand = Brand.create(name, coo)
        print(f'Success: {brand.name, brand.coo}')
    except Exception as exc:
        print("Error creating brand: ", exc)

def delete_brand():
    brand_id = input("Enter the # of the brand to delete: ")
    
    if brand_id.isdigit():
        brand_id = int(brand_id)
        
        brand = Brand.find_by_id(brand_id)
        if brand:
            confirmation = input(f"Are you sure you want to delete the brand '{brand.name}'? Type and enter 'y' for yes, and 'n' for no: ")
            
            if confirmation.lower() == "y":
                brand.delete()
                print(f"Brand '{brand.name}' has been deleted.")
            else:
                print("Deletion canceled.")
        else:
            print(f"No car brand found with the # {brand_id}.")
    else:
        print("Invalid input. Please enter an existing brand #.")

def find_brand_by_name():
    name = input("Enter the brand's name: ")
    name = name.lower()
    brand = None
    for db_brand in Brand.get_all():
        if db_brand.name.lower() == name:
            brand = db_brand
            break

    if brand:
        print("ID", "\t", '{0: <15}'.format("BRAND NAME"), "\t", "COUNTRY OF ORIGIN")
        print(brand.id, "\t", '{0: <15}'.format(brand.name), "\t", brand.coo)
    else:
        print(f'Brand {name} not found')

def find_driver_by_name():
    name = input("Enter the driver's name: ")
    name = name.lower()
    for db_driver in Driver.get_all():
        if db_driver.name.lower() == name:
            driver = db_driver
            break

    if driver:
        print("DRIVER NAME")
        print(driver.name)
    else:
        print(f'Driver {name} not found')

def list_brands_by_country():
    country = input("Enter the country of origin: ")
    country = country.lower()
    brands = [brand for brand in Brand.get_all() if brand.coo.lower() == country]
    if brands:
        print(f"Car brands from {country}:")
        print("ID", "\t", '{0: <15}'.format("BRAND NAME"))
        for brand in brands:
            print(brand.id, "\t", '{0: <15}'.format(brand.name))
    else:
        print(f"No car brands found from {country}.")

def create_driver():
   name = input("Enter the driver's name: ")
   brand_num = input("Enter the driver's car #: ")
   try:
       brand_num = int(brand_num)
       driver = Driver.create(name, brand_num)
       print(f'Success: {driver}')
   except ValueError as ve:
       print("Error creating driver: The Driver's Brand # must the Brand # of an existing Brand in our database")
   except Exception as exc:
       print("Error creating driver: ", exc)

def create_driver():
    name = input("Enter the driver's name: ")
    brand_num = input("Enter the driver's car #: ")
    driver_password = input("Set a password for the driver: ")

    try:
        brand_num = int(brand_num)
        driver = Driver.create(name, brand_num)
        drivers[driver.id] = driver_password  # Store driver and associated password
        print(f'Driver "{driver.name}" created with car #{driver.brand_num}.')
    except ValueError as ve:
        print("Error creating driver: The Driver's Brand # must be the Brand # of an existing Brand in our database.")
    except Exception as exc:
        print("Error creating driver:", exc)

def list_drivers():
    drivers = Driver.get_all()
    for driver in drivers:
        print("DRIVER NAME", "\t", "CAR NUMBER")
        print(driver.name, "\t", driver.brand_num)

drivers = {}

def delete_driver():
    driver_id = input("Please Enter the Driver # You Wish To Delete: ")

    if driver_id.isdigit():
        driver_id = int(driver_id)
        entered_password = input(f"Enter the password for Driver #{driver_id}: ")

        if drivers.get(driver_id) == entered_password: 
            driver = Driver.find_by_id(driver_id)

            if driver:
                confirmation = input(f"Are you sure you want to delete the driver '{driver.name}'? Type and enter 'y' for yes, and 'n' for no: ")

                if confirmation.lower() == "y":
                    driver.delete()
                    del drivers[driver_id]  
                    print(f"Driver '{driver.name}' has been deleted.")
                else:
                    print("Deletion canceled.")
            else:
                print(f"No driver found with the # {driver_id}.")
        else:
            print("Password Incorrect. Driver has Not Been Deleted")
    else:
        print("Invalid input. Please enter a valid driver #.")

def list_drivers_by_brand():
    brand_num = input("Enter the brand number to list drivers: ")
    if brand_num.isdigit():
        brand_num = int(brand_num)
        drivers = [driver for driver in Driver.get_all() if driver.brand_num == brand_num]
        if drivers:
            print(f"Drivers with brand number {brand_num}:")
            for driver in drivers:
                print(driver)
        else:
            print(f"No drivers found with brand number {brand_num}.")
    else:
        print("Invalid input. Please enter a valid brand number.")


def find_brand_by_driver_name():
    name = input("Enter the driver's name: ")
    name = name.lower()
    for db_driver in Driver.get_all():
        if db_driver.name.lower() == name:
            driver = db_driver
            break

    if driver:
        print("DRIVER CAR NUMBER")
        print(driver.brand_num)
    else:
        print(f'Driver {name} not found')
