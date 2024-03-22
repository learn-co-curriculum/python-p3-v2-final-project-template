# cli_visits.py
#? Copied logic from cli_restaurants.py
#! TODO - Implement menu items for visits
import click

@click.group()
def visits():
    """Visits commands."""
    pass

@visits.command()
def view_all():
    """View all visits."""
    pass

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
    click.echo("\nvisits Menu:")
    click.echo("1: View All")
    click.echo("2: Filter by Cuisine")
    click.echo("3: Filter by Location")
    click.echo("x: Back to Main Menu")

    visits_options = {
        '1': view_all,
        '2': filter_by_cuisine,
        '3': filter_by_location,
    }

    while True:
        choice = click.prompt("Please enter your choice", type=str)

        if choice in visits_options:
            click.clear()
            visits_options[choice]()  # Invoke the chosen function
        elif choice == 'x':
            click.clear()
            break #exit the visits_menu
        else:
            click.echo("Invalid choice. Please try again.")