import click
from rich import print

from cli.pages import (
    define_page,
    navigate,
    go_back,
    draw_page,
    handle_user_input,
    exit_program,
    pages,
    current_page,
    previous_pages,
)
from cli.user_account_page import user_account_page
from cli.restaurants_page import restaurants_page
from cli.visits_page import visits_page

@click.command()
def main():
    # Define pages
    home_page = define_page("home", "Home")
    home_page.add_option("User Account", lambda: navigate("user_account"))
    home_page.add_option("Restaurants", lambda: navigate("restaurants"))
    home_page.add_option("Visits", lambda: navigate("visits"))

    navigate("home")

    while True:
        draw_page()
        user_input = click.prompt("Enter your choice").lower()
        handle_user_input(user_input)

if __name__ == "__main__":
    main()