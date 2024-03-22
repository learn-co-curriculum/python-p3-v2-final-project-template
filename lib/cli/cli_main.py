# lib/cli.py
import click
from cli_visits import visits
from cli_user import user_account_menu
from cli_restaurants import restaurants



def show_main_menu():
    click.echo("\nMain Menu:")
    click.echo("1: View User Account")
    click.echo("2: View Restaurants")
    click.echo("3: View Visits")
    click.echo("4: Exit")


def main_menu():
    menu_options = {
        '1': user_account_menu,  
        '2': restaurants,   
        '3': visits,        
    }

    while True:
        show_main_menu()
        choice = click.prompt("Please enter your choice", type=str)

        if choice in menu_options:
            click.clear()
            menu_options[choice]()
        elif choice == '4':
            click.echo("Goodbye!")
            break
        else:
            click.clear()
            click.echo("Invalid choice. Please try again.")
if __name__ == '__main__':
    main_menu()