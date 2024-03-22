# cli_restaurants.py
import click
from classes.Restaurant import Restaurant


@click.group()
def restaurants():
    """Restaurants commands."""
    pass

@restaurants.command()
def view_all_restaurants():
    """View all restaurants."""
    def next_page():
        click.echo('Next Page')

    def prev_page():
        click.echo('Previous Page')

    all = Restaurant.get_all()

    #limit search by 20
    restaurants = all[0:20]

    #print the name and cuisine 
    for restaurant in restaurants:
        click.echo(f"{restaurant.id}. {restaurant.name} || {restaurant.cuisine}")
        
    click.echo("\nRestaurants Menu:")
    click.echo("1: Next Page")
    click.echo("2: Previous Page")
    click.echo("x: Back to Main Menu")

    view_all_options = {
        '1': next_page,
        '2': prev_page
    }

    while True:
        choice = click.prompt("Please enter your choice", type=str)

        if choice in view_all_options:
            click.clear()
            view_all_options[choice]()  # Invoke the chosen function
        elif choice == 'x':
            click.clear()
            break #exit the restaurants_menu
        else:
            click.echo("Invalid choice. Please try again.")


@restaurants.command()
def filter_by_cuisine():
    """Filter restaurants by cuisine."""
    pass

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
        '1': view_all_restaurants,
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