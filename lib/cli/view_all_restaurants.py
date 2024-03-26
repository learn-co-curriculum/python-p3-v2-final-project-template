import click
from classes.Restaurant import Restaurant
from rich import print

def display_restaurants(page_number):
    restaurants_per_page = 10
    offset = (page_number - 1) * restaurants_per_page
    restaurants = Restaurant.get_all(limit=restaurants_per_page, offset=offset)
    total_restaurants = Restaurant.get_total_count()
    total_pages = (total_restaurants + restaurants_per_page - 1) // restaurants_per_page

    click.clear()
    print("[bold #FF7EF5 ]All Restaurants[/bold #FF7EF5]")
    print("[white]=[/white]" * 20)

    if not restaurants:
        print("No restaurants found.")
    else:
        print(f"Displaying restaurants {offset + 1} - {offset + len(restaurants)} of {total_restaurants}")
        for restaurant in restaurants:
            print(f"[#FF7EF5]Name:[/#FF7EF5] [white]{restaurant.name}[/white] [purple]Cuisine:[/purple] [white]{restaurant.cuisine}[/white] [green]Price:[/green] [white]{restaurant.price} [/white] [red]Award:[/red] [white]{restaurant.award}[/white]")
            print(f"[blue]Description[/blue]:[white]{restaurant.description[0:120]}...[/white]")
            print("---")
    print(f"\nPage {page_number} of {total_pages}")