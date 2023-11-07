# lib/cli.py
from models.Parent import Parent,Child
from simple_term_menu import TerminalMenu


p1=Parent('Zeus - God of Thunder','this is a bio')
p2=Parent('Poseidon - God of The Seas', 'Poseidon Bio')
p3=Parent('Hades - God of The Underworld', ' Hades Bio')
p4=Parent('Hera - Goddess of Marriage', "Hera Bio")
p5=Parent('Heistia - Goddess of The House', 'Heistia Bio')
p6=Parent('Demeter - Goddess of The Harvest', 'Demeter Bio')
c1=Child('Athena - God of Wisdom','Athena bio',p1)

options = [" [q] Quit", "[a] List of All Gods"]

mainMenu = TerminalMenu(options)
subMenu = TerminalMenu( ["[q] Quit", f'{Parent.name_list}', f'{Child.name_list}'], title = "Sub-Menu")

quitting = False
while quitting ==  False:
    optionsIndex = mainMenu.show()
    optionsChoice = options[optionsIndex]
    if optionsChoice == "[q] Quit":
        exit_program()
    if optionsChoice == "[a] List of All Gods":
        subMenu.show()
    else:
        print(optionsChoice)







from helpers import (
    exit_program
)


# def main():
#     while True:
#         menu()
#         choice = input("> ")
#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             print(f'{Parent.all_parents}{Child.spawn}')
#         else:
#             print("Invalid choice")


# def menu():
#     print("Please select an option:")
#     print("0. Exit the program")
#     print("1. Here is a list of all Gods you can look up.")


# if __name__ == "__main__":
#     main()
