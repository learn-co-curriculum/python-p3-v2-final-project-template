from cli.pages import define_page

restaurants_page = define_page("restaurants", "Restaurants")
# Add options for restaurants page
restaurants_page.add_option("Option 1", lambda: print("Restaurants - Option 1"))
restaurants_page.add_option("Option 2", lambda: print("Restaurants - Option 2"))