# lib/cli.py
import click
from cli.cli_visits import visits_menu
from cli.cli_user import user_account_menu
from cli.cli_restaurants import restaurants_menu



def show_main_menu():
    click.echo("\nMain Menu:")
    click.echo("1: View User Account")
    click.echo("2: View Restaurants")
    click.echo("3: View Visits")
    click.echo("4: Exit Program")


def main_menu():
    menu_options = {
        '1': user_account_menu,  
        '2': restaurants_menu,   
        '3': visits_menu,        
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