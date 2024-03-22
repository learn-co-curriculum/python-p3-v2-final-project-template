# cli_restaurants.py
import click

@click.group()
def restaurants():
    """Restaurants commands. This is a placeholder for the group."""
    pass

@restaurants.command()
def view_all():
    """View all restaurants."""
    pass

@restaurants.command()
def filter_by_cuisine():
    """Filter restaurants by cuisine."""
    

@restaurants.command()
def filter_by_location():
    """Filter restaurants by location."""
    click.echo("Restaurants filtered by location.")

def restaurants_menu():
    """Displays the restaurants menu and prompts for action."""
    click.echo("\nRestaurants Menu:")
    click.echo("1: View All")
    click.echo("2: Filter by Cuisine")
    click.echo("3: Filter by Location")
    click.echo("x: Back to Main Menu")

    restaurants_options = {
        '1': view_all,
        '2': filter_by_cuisine,
        '3': filter_by_location,
    }

    while True:
        choice = click.prompt("Please enter your choice", type=str)

        if choice in restaurants_options:
            click.clear()
            restaurants_options[choice]()  # Invoke the chosen function
        elif choice == 'x':
            click.clear()
            break #exit the restaurants_menu
        else:
            click.echo("Invalid choice. Please try again.")