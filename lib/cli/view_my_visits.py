import click
from rich import print
from cli.pages import navigate
from classes.User import User
from classes.Visit import Visit
from classes.Restaurant import Restaurant

def view_visit(visit_id):
    exit = False
    visit = Visit.get_visit_by_id(visit_id)

    print(f'\n{visit.description}')
    print(f'\n{visit.rating}')
    print(f'\n{visit.date}\n')
    print('=' * 20)

    while not exit:

        choice = click.prompt(f'Edit or Delete visit? (d/e)')
        if choice == 'd':
            confirmation = click.prompt('\nAre you sure you want to delete this visit? (y/n)')
            if confirmation == 'y':
                visit.delete()
                print('\nVisit has been deleted')
                click.pause()
                exit = True
                navigate('home')
            elif confirmation == 'n':
                print('\nAborting delete')
                click.pause()
                exit = True
            else:
                print('Please use a valid input')
        elif choice == 'e':

            edit_choice = click.prompt('\nWhat would you like to change? (1.Rating, 2.Date, 3.Description )')

            if edit_choice == '1':
                rating = click.prompt(f'\nChange rating from {visit.rating} to')
                visit.rating = int(rating)
                visit.update()
                print('\nUpdated Rating')
                click.pause()
                exit = True
            elif edit_choice == '2':
                date = click.prompt(f'\nChange rating from {visit.date} to... ')
                visit.date = date
                visit.update()
                print('\nUpdated Date')
                click.pause()
                exit = True
            elif edit_choice == '3':
                description = click.prompt(f'\nChange rating from {visit.description[0:20]} to... ')
                visit.description = description
                visit.update()
                print('\nUpdated Description')
                click.pause()
                exit = True
            else:
                print('\nPlease use a valid input')
        else:
            print('\nPlease use a valid input')






def display_my_visits():
    from cli.visits_page import visits_page

    exit = False

    user = User.current_user.visits()
    visits_page.options = []


    for visit in user:
        restaurant_obj = Restaurant.get_by_id(visit.restaurant_id)
        visits_page.add_option(f'[yellow]{visit.date}[/yellow] Rating: {visit.rating} <"{visit.description[0:20]}..."> [#FF7EF5]{restaurant_obj.name}[/#FF7EF5] in [blue]{restaurant_obj.ward}[/blue]', lambda visit_id = visit._id: view_visit(visit_id))
        # print(f'\n{visit.date} Rating: {visit.rating} <"{visit.description[0:20]}..."> [#FF7EF5]{restaurant_obj.name}[/#FF7EF5] in [blue]{restaurant_obj.ward}[/blue]')

    return user
        

    

