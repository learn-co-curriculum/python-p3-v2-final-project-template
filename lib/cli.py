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
godOptions = ["[q] Quit","[a] Bio", "[b] Children"]
subMenuOptions =[ "[q] Quit",f"[a] {p1.name}",f"[b] {p2.name}",f"[c] {p3.name}",f"[d] {p4.name}",f"[e] {p5.name}",f"[f] {p6.name}",f"[g] {c1.name}"]

mainMenu = TerminalMenu(options)
subMenu = TerminalMenu( subMenuOptions, title = "Sub-Menu")
GodSubMenu= TerminalMenu(godOptions, title = 'God SubMenu')

quitting = False

while quitting ==  False:
    optionsIndex = mainMenu.show()
    optionsChoice = options[optionsIndex]
  
    if optionsChoice == "[q] Quit":
        exit_program()

    if optionsChoice == "[a] List of All Gods":
        subMenuIndex= subMenu.show()
        subMenuChoice = subMenuOptions[subMenuIndex]

        if subMenuChoice == "[a] Zeus - God of Thunder":
            GodSubMenu.show()
            godOptionIndex = GodSubMenu.show()
            godOptionChoice = godOptions[godOptionIndex]
    
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
