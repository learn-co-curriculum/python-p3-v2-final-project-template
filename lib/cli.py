# lib/cli.py

from helpers import (
    exit_program,
    age_checker
)


def main():
    while True:
        enter_bar()
            
        option_select()
        
#verifies valid choice
def get_valid_choice(valid_options):
    #keep asking until a valid choice is entered
    while True:
        choice = input("> ")
        if choice in valid_options:
            return choice
        print("Invalid choice, please try again")

#entering the bar
def enter_bar():
    print("\nPlease select an option:")
    print("0. Leave")
    print("1. Can I see your ID?")

    choice = get_valid_choice(["0", "1"])
    if choice == "0":
        exit_program()
    elif choice == "1":
        age_checker()

#main option select
def option_select():
    print("\n Options")
    #change later to only show if tab is open
    print("0. Close Your Tab")
    print("1. Can I get a drink?")
    #hint for leaving if your tab is open
    print("\nhint: to leave, close your tab")

    choice = get_valid_choice(["0", "1"])
    if choice == "0":
        close_tab()
    elif choice == "1":
        select_drink()

#drink selection options
def select_drink():
    print("\n Options:")
    print("0. Go Back")
    print("1. Cosmo")
    print("2. Manhattan")
    print("3. Tequila Sunrise")
    print("4. Rum Runner")
    print("5. Bees Knees")

    choice = get_valid_choice(["0", "1", "2", "3", "4", "5"])
    if choice == "0":
        option_select()
    else:
        drinks = {
            "1": "Cosmo",
            "2": "Manhattan",
            "3": "Tequila Sunrise",
            "4": "Rum Runner",
            "5": "Bees Knees"
        }
    print(f"\n{drinks[choice]}, right up!")
    open_tab()

def open_tab():
    print("Would you like to open a tab?")
    print("0. yes")
    print("1. no")

    choice = get_valid_choice(["0", "1"])
    if choice == "0":
        print("Opening tab!")
    else:
        print("Here's your total: total")
    
    print("Press enter to continue")
    user_input = input()
    option_select()

#shows option to close tab, change later to show up if drinks are added to tab
def close_tab():
    print("\n Are you sure?:")
    print("0. Yes")
    print("1. No")

    choice = get_valid_choice(["0", "1"])
    if choice == "0":
        leave_bar()
    elif choice == "1":
        option_select()

#leaving the bar
def leave_bar():
    #show this if just closing tab
    print("\nClosing Tab!")
    print(" Would you like to leave?")
    print("0. yes")
    print("1. no")

    choice = get_valid_choice(["0", "1"])
    if choice == "0":
        exit_program()
    elif choice == "1":
        option_select()


if __name__ == "__main__":
    main()
