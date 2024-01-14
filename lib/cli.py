# lib/cli.py
from rich.console import Console
console = Console()

from helpers import (
    exit_program,
    add_member,
    change_membership, 
    view_members,
    view_all_programs,
    add_program,
    delete_member, 
    delete_program,
    add_trainer,
    delete_trainer
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_member()
        elif choice == "2":
            change_membership()
        elif choice == "3":
            view_members()
        elif choice == "4":
            view_all_programs()
        elif choice == "5":
            add_program()
        elif choice == "6":
            delete_member()
        elif choice == "7":
            delete_program()
        elif choice == "8":
            add_trainer()
        elif choice == "9":
            delete_trainer()
        else:
            print("Invalid choice")


def menu():
    console.print("____________________________________", style="bold green")
    console.print("       VVVV               VVVV        ")
    console.print("       (__)               (__)")
    console.print("        \ \               / /")
    console.print("         \ \   \\|||//   / /")
    console.print("          > \   _   _   / <")
    console.print("           > \ / \ / \ / <", style="bold green")
    console.print("             > \\_o_o_// <")
    console.print("             > ( (_) ) <", style="bold green")
    console.print("              >|     |<")
    console.print("             / |\___/| \ ", style="bold green")
    console.print("             / (_____) \ ")
    console.print("             /         \ ")
    console.print("              /   o   \ ", style="bold green")
    console.print("               ) ___ (   ")
    console.print("              / /   \ \  ", style="bold green")
    console.print("             ( /     \ )")
    console.print("             ><       ><")
    console.print("            ///\     /\\\\", style="bold green")
    console.print("            '''       '''", style="bold green")
    
    console.print("Welcome to JKH Gym", style="bold blue")
    console.print("Please select an option:", style="bold")
    console.print("0. Exit the program")
    console.print("1. Add New Gym Member")
    console.print("2. Change Membership Plan")
    console.print("3. View Members")
    console.print("4. View All Programs")
    console.print("5. Add New Exercise Program")
    console.print("6. Delete Members")
    console.print("7. Delete Exercise Program")
    console.print("8. Add Trainer")
    console.print("9. Delete Trainer")
print("Thank you for using JKH Gym.")

if __name__ == "__main__":
    main()
