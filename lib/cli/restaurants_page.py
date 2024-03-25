from cli.pages import define_page, navigate
from cli.view_all_restaurants import display_restaurants

def view_all_restaurants():
    navigate("view_all_restaurants")

def filter_by_cuisine():
    print("Filtering restaurants by cuisine...")
    # Add your logic here to filter restaurants by cuisine

def filter_by_location():
    print("Filtering restaurants by location...")
    # Add your logic here to filter restaurants by location

restaurants_page = define_page("restaurants", "Restaurants")
restaurants_page.add_option("View All Restaurants", view_all_restaurants)
restaurants_page.add_option("Filter by Cuisine", filter_by_cuisine)
restaurants_page.add_option("Filter by Location", filter_by_location)