import click
from classes.Restaurant import Restaurant
from classes.Visit import Visit
from cli.pages import navigate
from classes.User import User

def display_restaurants(restaurants, page_number, total_restaurants, total_pages):
    click.clear()
    click.echo("Restaurants")
    click.echo("=" * 20)

    if not restaurants:
        print("No restaurants found.")
    else:
        print(f"Displaying restaurants {(page_number - 1) * 10 + 1} - {min(page_number * 10, total_restaurants)} of {total_restaurants}")
        for restaurant in restaurants:
            print(f"{restaurant.id}. {restaurant.name} || Location: {restaurant.ward} || Cuisine: {restaurant.cuisine}")
            print("---")

    print(f"\nPage {page_number} of {total_pages}")

def select_restaurant(restaurant_id):
    restaurant = Restaurant.get_by_id(restaurant_id)
    if restaurant:
        display_restaurant_details(restaurant)
    else:
        click.echo("Invalid restaurant number. Please try again.")

def display_restaurant_details(restaurant):
    click.clear()
    click.echo("Restaurant Details")
    click.echo("=" * 20)
    click.echo(f"Name: {restaurant.name}")
    click.echo(f"Cuisine: {restaurant.cuisine}")
    click.echo(f"Address: {restaurant.address}")
    click.echo(f"Ward: {restaurant.ward}")
    click.echo(f"Price: {restaurant.price}")
    click.echo(f"Website: {restaurant.website}")
    click.echo(f"Award: {restaurant.award}")
    click.echo(f"Misc: {restaurant.misc}")
    click.echo(f"Description: {restaurant.description}")
    click.echo("\nOptions:")
    click.echo("1. View Visits")
    click.echo("2. Add Visit")
    click.echo("3. Return to Restaurant List")
    choice = click.prompt("Enter your choice")
    if choice == "1":
        display_visits(restaurant.id)
    elif choice == "2":
        add_visit(restaurant.id)
    elif choice == "3":
        navigate("view_all_restaurants")
    else:
        click.echo("Invalid choice. Please try again.")
        display_restaurant_details(restaurant)

def display_visits(restaurant_id):
    rest_obj = Restaurant.get_by_id(restaurant_id)
    visits = rest_obj.visits()
    
    click.clear()
    click.echo("Visits")
    click.echo("=" * 20)

    if visits:
        for visit in visits:
            user_object = User.get_user_by_id(visit.user_id)
            visit_name = user_object.name
            click.echo(f"User: {visit_name}")
            click.echo(f"Description: {visit.description}")
            click.echo(f"Rating: {visit.rating}/10")
            click.echo(f"Date: {visit.date}")
            click.echo("---")
    else:
        click.echo("No visits found.")
    click.echo("\nPress any key to return to the restaurant details.")
    click.getchar()
    navigate("view_all_restaurants")

def add_visit(restaurant_id):


    click.clear()
    click.echo("Add Visit")
    click.echo("=" * 20)

    while True:
        try:
            rating = int(click.prompt("Enter your rating (1-10)"))
            if rating < 1 or rating > 10:
                raise ValueError
            break
        except ValueError:
            click.echo("Please enter a valid rating between 1 and 10.")

    description = click.prompt("Enter your description")
    #!Add Date Validation?
    date = click.prompt("Enter the visit date (MM-DD-YYYY)")
    user_id = User.current_user.id

    try:
        visit = Visit.create(rating, description, date, user_id, restaurant_id)
        click.echo("Visit added successfully!")
        click.pause()
        navigate("view_all_restaurants")
    except Exception as e:
        click.echo(f"An error occurred while adding the visit: {str(e)}")
        click.pause()