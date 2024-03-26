from cli.pages import define_page, navigate
from cli.view_all_restaurants import display_restaurants
from cli.filter_by_location import display_restaurants_by_location
from cli.filter_by_cuisine import display_restaurants_by_cuisine
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
    page_number = 1
    cuisine = ''

    while True:

        click.clear()
        print('Choose a Cuisine Type')
        print('==================')
        print('\n')
        print('Chinese')
        print('---')
        print('French')
        print('---')
        print('Hispanic')
        print('---')
        print('Italian')
        print('---')
        print('Japanese')
        print('---')
        print('Sushi')
        print('---')
        print('Tempura')
        print('---')
        print('\n')

        choice = click.prompt('\nType your choice').lower()
        
        if choice == 'chinese':
            cuisine = 'Chinese'
            break
        elif choice == 'french':
            cuisine = 'French'
            break
        elif choice == 'hispanic':
            cuisine = 'Hispanic'
            break
        elif choice == 'italian':
            cuisine = 'Italian'
            break
        elif choice == 'japanese':
            cuisine = 'Japanese'
            break
        elif choice == 'sushi':
            cuisine = 'Sushi'
            break
        elif choice == 'tempura':
            cuisine = 'Tempura'
            break
        elif choice == 'x':
            navigate("restaurants")
            break
        else:
            print('\nPlease input a valid cuisine\n')
            click.pause()
            

    while True:

        click.clear()
        display_restaurants_by_cuisine(cuisine, page_number)
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