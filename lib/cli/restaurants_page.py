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

        click.clear()
        print('Choose a Location')
        print('==================')
        print('\n')
        print('Shibuya')
        print('---')
        print('Shinjuku')
        print('---')
        print('Bunkyo/Sumida/Taito')
        print('---')
        print('Chiyoda')
        print('---')
        print('Chuo')
        print('---')
        print('Meguro')
        print('---')
        print('Minato')
        print('---')
        print('Setagaya/Shinagawa')
        print('\n')

        choice = click.prompt('\nType your choice').lower()
        
        if choice == 'shibuya':
            location = 'Shibuya'
            break
        elif choice == 'shinjuku':
            location = 'Shinjuku'
            break
        elif choice == 'bunkyo/Sumida/Taito':
            location = 'Bunkyo/Sumida/Taito'
            break
        elif choice == 'chiyoda':
            location = 'Chiyoda'
            break
        elif choice == 'chuo':
            location = 'Chuo'
            break
        elif choice == 'minato':
            location = 'Minato'
            break
        elif choice == 'meguro':
            location = 'Meguro'
            break
        elif choice == 'setagaya/Shinagawa':
            location = 'Setagaya/Shinagawa'
            break
        elif choice == 'x':
            navigate("restaurants")
            break
        else:
            print('\nPlease input a valid location\n')
            click.pause()
            

    while True:

        click.clear()
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