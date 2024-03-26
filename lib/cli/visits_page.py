import click
from rich import print
from classes.User import User
from classes.Visit import Visit
from cli.pages import define_page


def view_visit(visit_id):
    global exit
    exit = False
    chosen_visit = Visit.get_visit_by_id(visit_id)

    while not exit:
        choice = click.prompt(f'\nEdit or Delete restaurant visit on {chosen_visit.date}? (e/d)').lower()
        if choice == 'd':
            delete_visit(chosen_visit)
        elif choice == 'e':
            edit_visit(chosen_visit)
            break
        else:
            print('Please enter a valid option')

def delete_visit(chosen_visit):
    pass

def edit_visit(chosen_visit):
    pass



visits_page = define_page("visits", "Visits")
# Add options for visits page

while current_user:
    visits = User.current_user.visits() 

print(visits)


# for visit in visits:

#     visits_page.add_option(f'{visit.date}', lambda: print("Visits - Option 1"))

# ... (Add more options as needed)

