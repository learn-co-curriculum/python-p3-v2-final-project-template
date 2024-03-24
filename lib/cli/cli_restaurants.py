# cli_restaurants.py
import click
from classes.Restaurant import Restaurant

@click.group()	
def restaurants():	
    """Restaurants commands."""	
    pass

@restaurants.command()
def filter_by_cuisine():
    """Filter restaurants by cuisine."""
    

@restaurants.command()
def filter_by_location():
    """Filter restaurants by location."""
    click.echo("Restaurants filtered by location.")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # => Restaurants Menu <=  # # # # # # # # # # # # # # #
def restaurants_menu():


    restaurants_options = {
        '1': view_all_restaurants,
        '2': filter_by_cuisine,
        '3': filter_by_location,
    }

    while True:
        """Displays the restaurants menu and prompts for action."""
        click.echo("\nRestaurants Menu:")
        click.echo("1: View All")
        click.echo("2: Filter by Cuisine")
        click.echo("3: Filter by Location")
        click.echo("x: Back to Main Menu")
        choice = click.prompt("Please enter your choice", type=str)

        if choice in restaurants_options:
            click.clear()
            restaurants_options[choice]()  # Invoke the chosen function
        elif choice == 'x':
            click.clear()
            break #exit the restaurants_menu
        else:
            click.clear()
            click.echo("Invalid choice. Please try again.")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # => 1. View All Restaurants <=  # # # # # # # # # # # # # 
def view_all_restaurants():
    """View all restaurants."""

    all = Restaurant.get_all()
    page = [0,20]
    restaurants = all[page[0]: page[1]]

    def parse_by_page():
        pass

    def next_page():
        p[0] += 20
        p[1] += 20
        restaurants = all[page[0]: page[1]]

    def prev_page():
        click.echo('Previous Page')


    #limit search by 20

    #print the name and cuisine 
    for restaurant in restaurants:
        click.echo(f"{restaurant.id}. {restaurant.name} || {restaurant.cuisine}")
        

    view_all_options = {
        '1': next_page,
        '2': prev_page
    }

    while True:
        click.echo("\nRestaurants Menu:")
        click.echo('#: View Restaurant by input')
        click.echo("Next: Next Page")
        click.echo("Prev: Previous Page")
        click.echo("x: Back to Main Menu")
        choice = click.prompt("Please enter your choice", type=str)

        if choice in view_all_options:
            click.clear()
            view_all_options[choice]()  # Invoke the chosen function
        elif choice == 'x':
            click.clear()
            break #exit the restaurants_menu
        else:
            click.clear()
            click.echo("Invalid choice. Please try again.")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # => 2. Filter By Cuisine <=  # # # # # # # # # # # # # 

def filter_by_cuisine():
    """Filter restaurants by cuisine."""
    click.echo("Restaurants filtered by cuisine.")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # => 3. Filter By Location <=  # # # # # # # # # # # # # 

def filter_by_location():
    """Filter restaurants by location."""
    click.echo("Restaurants filtered by location.")