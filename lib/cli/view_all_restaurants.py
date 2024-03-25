from cli.pages import define_page, navigate
from classes.Restaurant import Restaurant

def display_restaurants(page_number):
    restaurants_per_page = 10
    offset = (page_number - 1) * restaurants_per_page
    restaurants = Restaurant.get_all(limit=restaurants_per_page, offset=offset)
    total_restaurants = Restaurant.get_total_count()
    total_pages = (total_restaurants + restaurants_per_page - 1) // restaurants_per_page

    if not restaurants:
        print("No restaurants found.")
    else:
        print(f"Displaying restaurants {offset + 1} - {offset + len(restaurants)} of {total_restaurants}")
        for restaurant in restaurants:
            print(f"Name: {restaurant.name}")
            print(f"Description: {restaurant.description}")
            print("---")

    print(f"Page {page_number} of {total_pages}")
    if page_number > 1:
        print("p. Previous Page")
    if page_number < total_pages:
        print("n. Next Page")

def handle_page_navigation(page_number):
    user_input = input("Enter your choice: ")
    if user_input == 'p' and page_number > 1:
        navigate("view_all_restaurants", page_number - 1)
    elif user_input == 'n' and page_number < Restaurant.get_total_pages(10):
        navigate("view_all_restaurants", page_number + 1)
    else:
        print("Invalid choice. Please try again.")
        handle_page_navigation(page_number)

view_all_restaurants_page = define_page("view_all_restaurants", "All Restaurants")
view_all_restaurants_page.add_option("Display Restaurants", lambda: display_restaurants(1))
view_all_restaurants_page.add_option("Back", lambda: navigate("restaurants"))
view_all_restaurants_page.add_option("Navigate Pages", lambda: handle_page_navigation(1))