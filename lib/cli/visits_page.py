import click
from rich import print
from classes.User import User
from classes.Visit import Visit
from cli.pages import define_page
from cli.view_my_visits import display_my_visits





visits_page = define_page("visits", "Visits")

visits_page.add_option('View My Visits', lambda: display_my_visits() )


