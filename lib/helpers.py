# lib/helpers.py
# from debug import Jay
# from debug import Victoria
# from debug import Kerissa
# from debug import Madison
# from debug import Johnathan

from colorama import Fore, Style, init
from models.Customer import Customer

init()

def customer_name():
    while True:
        name = input("Enter name (1-10 characters): ").strip()
        try:
            customer = Customer(name=name, age=25)
            return customer
        except (ValueError, TypeError) as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)
            print(Fore.CYAN + "Please enter a valid name." + Style.RESET_ALL)

def customer_age(customer):
    while True:
        age = input("Enter your age: ")
        try:
            customer.age = int(age)
            customer.save()
            return customer.age
        except(ValueError, TypeError) as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)
            print(Fore.CYAN + "Please enter a valid age." + Style.RESET_ALL)

def age_checker(customer):
    if customer.age >= 21:
        print(Fore.GREEN + "\nWelcome in!" + Style.RESET_ALL)
    else:
        delete_customer(customer)
        print(Fore.RED + "\nSorry gotta go!" + Style.RESET_ALL)
        exit()


def exit_program(customer):
    delete_customer(customer)
    print(Fore.GREEN + "\n See ya later!" + Style.RESET_ALL)
    exit()

def delete_customer(customer):
    if customer:
        customer.delete()