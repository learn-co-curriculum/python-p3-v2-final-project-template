import click
from rich import print
from classes.User import User
from classes.Visit import Visit
from cli.pages import define_page


def view_visit(visit_id):
    global exit
    exit = False
    chosen_visit = Visit.get_visit_by_id(visit_id)



visits_page = define_page("visits", "Visits")
# Add options for visits page
visits_page.add_option("Option 1", lambda: print("Visits - Option 1"))
visits_page.add_option("Option 2", lambda: print("Visits - Option 2"))
# ... (Add more options as needed)

