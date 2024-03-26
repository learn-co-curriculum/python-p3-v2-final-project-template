from cli.pages import define_page, navigate
from classes.Restaurant import Restaurant
from cli.restaurant_utils import display_restaurants, select_restaurant
import click
from rich import print
import click

def view_all_restaurants():
    page_number = 1
    while True:
        restaurants_per_page = 10
        offset = (page_number - 1) * restaurants_per_page
        restaurants = Restaurant.get_all(limit=restaurants_per_page, offset=offset)
        total_restaurants = Restaurant.get_total_count()
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

def filter_by_cuisine():
    page_number = 1
    cuisine = ''

    while True:
        click.clear()
        print('[bold #FF7EF5]Choose a Cuisine Type[/bold #FF7EF5]')
        print('==================')
        print('\n')
        print('1. Chinese')
        print('---')
        print('2. French')
        print('---')
        print('3. Hispanic')
        print('---')
        print('4. Italian')
        print('---')
        print('5. Japanese')
        print('---')
        print('6. Sushi')
        print('---')
        print('7. Tempura')
        print('---')
        print('\n')

        choice = click.prompt('\nType your choice').lower()
        
        if choice == 'chinese' or choice == '1':
            cuisine = 'Chinese'
            break
        elif choice == 'french' or choice == '2':
            cuisine = 'French'
            break
        elif choice == 'hispanic' or choice == '3':
            cuisine = 'Hispanic'
            break
        elif choice == 'italian' or choice == '4':
            cuisine = 'Italian'
            break
        elif choice == 'japanese' or choice == '5':
            cuisine = 'Japanese'
            break
        elif choice == 'sushi' or choice == '6':
            cuisine = 'Sushi'
            break
        elif choice == 'tempura' or choice == '7':
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

def filter_by_location():
    page_number = 1
    location = ''

    while True:
        click.clear()
        print('[bold #FF7EF5]Choose a Location[/bold #FF7EF5]')
        print('==================')
        print('\n')
        print('1. Shibuya')
        print('---')
        print('2. Shinjuku')
        print('---')
        print('3. Bunkyo/Sumida/Taito')
        print('---')
        print('4. Chiyoda')
        print('---')
        print('5. Chuo')
        print('---')
        print('6. Meguro')
        print('---')
        print('7. Minato')
        print('---')
        print('8. Setagaya/Shinagawa')
        print('\n')

        choice = click.prompt('\nType your choice').lower()
        
        if choice == 'shibuya' or choice == '1':
            location = 'Shibuya'
            break
        elif choice == 'shinjuku' or choice == '2':
            location = 'Shinjuku'
            break
        elif choice == 'bunkyo/sumida/taito' or choice == '3':
            location = 'Bunkyo/Sumida/Taito'
            break
        elif choice == 'chiyoda' or choice == '4':
            location = 'Chiyoda'
            break
        elif choice == 'chuo' or choice == '5':
            location = 'Chuo'
            break
        elif choice == 'minato' or choice == '6':
            location = 'Minato'
            break
        elif choice == 'meguro' or choice == '7':
            location = 'Meguro'
            break
        elif choice == 'setagaya/shinagawa' or choice == '8':
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
        restaurants_per_page = 10
        offset = (page_number - 1) * restaurants_per_page
        restaurants = Restaurant.get_restaurants_by_location(location, limit=restaurants_per_page, offset=offset)
        total_restaurants = Restaurant.get_count_by_location(location)
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

restaurants_page = define_page("restaurants", "Restaurants")
restaurants_page.add_option("View All Restaurants", view_all_restaurants)
restaurants_page.add_option("Filter by Cuisine", filter_by_cuisine)
restaurants_page.add_option("Filter by Location", filter_by_location)
restaurants_page.add_option("Back", lambda: navigate("home"))