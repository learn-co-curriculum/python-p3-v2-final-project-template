from cli.pages import define_page, navigate
from cli.view_all_restaurants import display_restaurants
from cli.filter_by_location import display_restaurants_by_location
import click

def view_all_restaurants():
    page_number = 1
    while True:
        display_restaurants(page_number)
        choice = click.prompt("\nEnter your choice (p: Previous Page, n: Next Page, x: Back to Restaurants Menu)")
        if choice == 'p' and page_number > 1:
            page_number -= 1
        elif choice == 'n':
            page_number += 1
        elif choice == 'x':
            navigate("restaurants")
            break
        else:
            click.echo("Invalid choice. Please try again.")

def filter_by_cuisine():
    click.echo("Restaurants filtered by cuisine.")

def filter_by_location():
    page_number = 1
    location = ''

    while True:
        print('Shibuya')
        print('Shinjuku')
        print('FUCHU')
        choice = click.prompt('\nType your choice')
        if choice == 'Shibuya':
            location = 'Shibuya'
            break
        elif choice == 'Shinjuku':
            location = 'Shinjuku'
            break
        else:
            click.echo('Please input a valid location')
            

    while True:
        display_restaurants_by_location(location, page_number)
        choice = click.prompt("\nEnter your choice (p: Previous Page, n: Next Page, x: Back to Restaurants Menu)")
        if choice == 'p' and page_number > 1:
            page_number -= 1
        elif choice == 'n':
            page_number += 1
        elif choice == 'x':
            navigate("restaurants")
            break
        else:
            click.echo("Invalid choice. Please try again.")

restaurants_page = define_page("restaurants", "Restaurants")
restaurants_page.add_option("View All Restaurants", view_all_restaurants)
restaurants_page.add_option("Filter by Cuisine", filter_by_cuisine)
restaurants_page.add_option("Filter by Location", filter_by_location)
restaurants_page.add_option("Back", lambda: navigate("home"))