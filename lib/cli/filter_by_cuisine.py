import click
from classes.Restaurant import Restaurant
from cli.pages import define_page, navigate
from cli.restaurant_utils import display_restaurants, select_restaurant

def filter_by_cuisine_input():
    cuisine = click.prompt("Enter the cuisine to filter by")
    page_number = 1
    while True:
        restaurants_per_page = 10
        offset = (page_number - 1) * restaurants_per_page
        restaurants = Restaurant.get_restaurants_by_cuisine(cuisine, limit=restaurants_per_page, offset=offset)
        total_restaurants = Restaurant.get_count_by_cuisine(cuisine)
        total_pages = (total_restaurants + restaurants_per_page - 1) // restaurants_per_page

        display_restaurants(restaurants, page_number, total_restaurants, total_pages)

        choice = click.prompt("\nEnter your choice (p: Previous Page, n: Next Page, x: Back to Restaurants Menu, #: Select Restaurant)")
        if choice.lower() == 'p' and page_number > 1:
            page_number -= 1
        elif choice.lower() == 'n' and page_number < total_pages:
            page_number += 1
        elif choice.lower() == 'x':
            navigate("restaurants")
            break
        else:
            select_restaurant(choice)

filter_by_cuisine_page = define_page("filter_by_cuisine", "Filter by Cuisine")
filter_by_cuisine_page.add_option("Enter Cuisine", filter_by_cuisine_input)
filter_by_cuisine_page.add_option("Back", lambda: navigate("restaurants"))