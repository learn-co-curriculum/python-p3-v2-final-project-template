# lib/cli.py
from rich.console import Console

#from helpers import (
    #exit_program,
    #helper_1
#)

console = Console()

#def main():
    #while True:
        #menu()
        #choice = input("> ")
        #if choice == "0":
            #exit_program()
        #elif choice == "1":
            #helper_1()
        #else:
            #print("Invalid choice")

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
    
    console.print("Welcome to JKH Gym", style="bold purple")
    console.print("Please select an option:", style="bold")
    console.print("0. Exit the program")
    console.print("1. Some useful function")
    console.print("2. Manage Members")
    console.print("3. Schedule Classes")
    console.print("4. Manege Trainer")
    console.print("5. Manage Exercise")

menu()
option = int(input("Select an option: "))

while option != 0:
    if option == 1:
        #open some useful function
        print("Option 1 has been called")
    elif option == 2:
        #open manage members
        print("Option 2 has been called")
    elif option == 3:
        #open schedule classes
        print("Option 3 has been called")
    elif option == 4:
        #open manage trainer
        print("Option 4 has been called")
    elif option == 5:
        #open manage exercise
        print("Option 5 has been called")
    else:
        print("Invalid option")
    
    print()
    menu()
    option = int(input("Select an option: "))

print("Thank you for using JKH Gym. Goodbye.")



if __name__ == "__main__":
    main()
