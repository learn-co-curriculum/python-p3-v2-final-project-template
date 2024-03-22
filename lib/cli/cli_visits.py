# cli_visits.py
#? Copied logic from cli_restaurants.py
#! TODO - Implement menu items for visits
import click
from classes.Visit import Visit
#import cli_visits_all
@click.group()
def visits():
    """Visits commands."""
    pass

@visits.command()
def view_all():
    """View all visits."""
    all = Visit.get_all()
    for visit in all:
        click.echo(visit.description)
    view_all_submenu()

@visits.command()
def filter_by_cuisine():
    """Filter visits by cuisine."""
    pass

@visits.command()
def filter_by_location():
    """Filter visits by location."""
    click.echo("visits filtered by location.")

def visits_menu():
    """Displays the visits menu and prompts for action."""
    

    visits_options = {
        '1': view_all,
        '2': filter_by_cuisine,
        '3': filter_by_location,
    }

    while True:
        click.echo("\nVisits Menu:")
        click.echo("1: View All")
        click.echo("2: Filter by Cuisine")
        click.echo("3: Filter by Location")
        click.echo("x: Back to Main Menu")
        choice = click.prompt("Please enter your choice", type=str)

        if choice in visits_options:
            click.clear()
            # Invoke the command function without triggering Click's standalone mode
            visits_options[choice].main(standalone_mode=False)
        elif choice == 'x':
            click.clear()
            break  # Return control back to the main menu
        else:
            click.echo("Invalid choice. Please try again.")


#Submenu for the 'View All' option.
def view_all_submenu():
    """Submenu for the 'View All' option."""
    while True:
        click.echo("\nView All Submenu:")
        click.echo("1: Return to Visits Menu")

        choice = click.prompt("Please enter your choice", type=str)

        if choice == '1':
            click.clear()
            break  # Exit the submenu and return to visits_menu
        else:
            click.echo("Invalid choice. Please try again.")